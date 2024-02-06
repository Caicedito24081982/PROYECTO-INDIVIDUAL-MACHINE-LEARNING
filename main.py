from fastapi import FastAPI, HTTPException
import pandas as pd
import gzip
import os
from typing import List, Dict

app = FastAPI()

@app.get("/developer/{desarrollador}")
async def developer_info(desarrollador: str) -> dict:
    ruta_archivo = r'C:\Users\ASUS\PI_ML_OPS\DATA\combined_data.json.gz'
    if not os.path.exists(ruta_archivo):
        raise HTTPException(status_code=404, detail="Archivo no encontrado.")
    try:
        with gzip.open(ruta_archivo, 'rt', encoding='utf-8') as f:
            df_clean = pd.read_json(f, lines=True)
        df_filtered = df_clean[df_clean['developer'].apply(lambda x: desarrollador.lower() in x.lower() if x is not None else False)].copy()
        if df_filtered.empty:
            raise HTTPException(status_code=404, detail=f"No se encontraron datos para el desarrollador {desarrollador}")
        df_filtered['release_date'] = pd.to_datetime(df_filtered['release_date'], errors='coerce')
        df_filtered['year'] = df_filtered['release_date'].dt.year
        df_summary = df_filtered.groupby('year').apply(lambda x: {
            "Cantidad de Items": len(x),
            "Contenido Free": f"{(x['price'] == 0).mean() * 100:.2f}%"
        }).reset_index(name='Estadisticas')
        return {
            "Desarrollador": desarrollador,
            "Estadísticas por año": df_summary.to_dict(orient='records')
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")
    
    

@app.get("/user_for_genre/{genero}")
async def user_for_genre(genero: str) -> dict:
    ruta_archivo = r'C:\Users\ASUS\PI_ML_OPS\DATA\combined_data.json.gz'
    if not os.path.exists(ruta_archivo):
        raise HTTPException(status_code=404, detail="Archivo no encontrado.")
    try:
        with gzip.open(ruta_archivo, 'rt', encoding='utf-8') as f:
            df_clean = pd.read_json(f, lines=True)

        # Verifica que las columnas necesarias existan
        required_columns = {'genres', 'playtime_forever', 'release_date', 'items_user_id'}
        if not required_columns.issubset(df_clean.columns):
            missing_columns = required_columns - set(df_clean.columns)
            raise HTTPException(
                status_code=500,
                detail=f"La columna(s) {', '.join(missing_columns)} no se encuentra en el DataFrame."
            )

        # Filtrar por género
        df_filtered = df_clean[df_clean['genres'].apply(lambda x: genero in x if x is not None else False)]
        if df_filtered.empty:
            raise HTTPException(status_code=404, detail=f"No se encontraron datos para el género {genero}")

        # Procesamiento de fechas y años
        df_filtered['release_date'] = pd.to_datetime(df_filtered['release_date'], errors='coerce')
        df_filtered['year'] = df_filtered['release_date'].dt.year

        # Calcular el usuario con más horas jugadas por género
        top_user = df_filtered.groupby('items_user_id')['playtime_forever'].sum().idxmax()
        if pd.isna(top_user):
            raise HTTPException(status_code=404, detail="No se encontraron usuarios para el género proporcionado.")

        # Calcular horas jugadas por año
        hours_by_year = df_filtered.groupby('year')['playtime_forever'].sum().reset_index(name='Horas')
        hours_by_year = hours_by_year.sort_values('year')

        return {
            f"Usuario con más horas jugadas para Género {genero}": top_user,
            "Horas jugadas": hours_by_year.to_dict(orient='records')
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")
    

@app.get("/best_developer_year/{year}")
async def best_developer_year(year: int) -> List[Dict[str, str]]:
    ruta_archivo = r'C:\Users\ASUS\PI_ML_OPS\DATA\combined_data.json.gz'
    if not os.path.exists(ruta_archivo):
        raise HTTPException(status_code=404, detail="Archivo no encontrado.")
    try:
        with gzip.open(ruta_archivo, 'rt', encoding='utf-8') as f:
            df_clean = pd.read_json(f, lines=True)
        
        # Asegurarse de que 'release_date' es de tipo datetime
        df_clean['release_date'] = pd.to_datetime(df_clean['release_date'], errors='coerce')

        # Filtrar filas donde 'release_date' es NaT (Not a Time)
        df_clean = df_clean.dropna(subset=['release_date'])

        # Verifica que las columnas necesarias existan
        required_columns = {'developer', 'release_date', 'recommend'}
        if not required_columns.issubset(df_clean.columns):
            missing_columns = required_columns - set(df_clean.columns)
            raise HTTPException(
                status_code=500,
                detail=f"La columna(s) {', '.join(missing_columns)} no se encuentra en el DataFrame."
            )

        # Filtrar por año y recomendaciones positivas
        df_filtered = df_clean[
            (df_clean['release_date'].dt.year == year) &
            (df_clean['recommend'] == True)
        ]

        if df_filtered.empty:
            raise HTTPException(status_code=404, detail=f"No se encontraron juegos recomendados en el año {year}")

        # Agrupar por desarrollador y contar recomendaciones positivas
        df_recommendations = df_filtered.groupby('developer').size().reset_index(name='recommendations')
        top_developers = df_recommendations.nlargest(3, 'recommendations').reset_index(drop=True)

        # Crear la respuesta
        response = [{f"Puesto {i+1}": row['developer']} for i, row in top_developers.iterrows()]
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")
    

@app.get("/developer_reviews_analysis/{desarrolladora}")
async def developer_reviews_analysis(desarrolladora: str) -> Dict[str, Dict[str, int]]:
    ruta_archivo = r'C:\Users\ASUS\PI_ML_OPS\DATA\combined_data.json.gz'
    if not os.path.exists(ruta_archivo):
        raise HTTPException(status_code=404, detail="Archivo no encontrado.")
    try:
        with gzip.open(ruta_archivo, 'rt', encoding='utf-8') as f:
            df_clean = pd.read_json(f, lines=True)

        # Verifica que las columnas necesarias existan
        required_columns = {'developer', 'sentiment_analysis'}
        if not required_columns.issubset(df_clean.columns):
            missing_columns = required_columns - set(df_clean.columns)
            raise HTTPException(
                status_code=500,
                detail=f"La columna(s) {', '.join(missing_columns)} no se encuentra en el DataFrame."
            )

        # Filtrar por desarrollador
        df_filtered = df_clean[df_clean['developer'].str.lower() == desarrolladora.lower()]
        if df_filtered.empty:
            return {desarrolladora: {"Negative": 0, "Positive": 0}}

        # Contar reseñas positivas y negativas basadas en el análisis de sentimiento
        sentiment_counts = df_filtered['sentiment_analysis'].value_counts().to_dict()

        # Asegurar que las claves "Positive" y "Negative" existan en el diccionario
        positive_reviews = sentiment_counts.get("Positive", 0)
        negative_reviews = sentiment_counts.get("Negative", 0)

        # Crear la respuesta ajustada al formato especificado
        response = {
            desarrolladora: {"Negative": negative_reviews, "Positive": positive_reviews}
        }
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")


@app.get("/userdata/{User_id}")
async def userdata(User_id: str) -> Dict[str, str]:
    ruta_archivo = r'C:\Users\ASUS\PI_ML_OPS\DATA\combined_data.json.gz'
    if not os.path.exists(ruta_archivo):
        raise HTTPException(status_code=404, detail="Archivo no encontrado.")
    try:
        with gzip.open(ruta_archivo, 'rt', encoding='utf-8') as f:
            df_clean = pd.read_json(f, lines=True)
        
        # Asegurarse de que 'items_user_id' y 'price' estén en df_clean y 'price' sea numérico
        df_clean['price'] = pd.to_numeric(df_clean['price'], errors='coerce').fillna(0)  # Convertir a numérico y manejar errores
        
        df_user = df_clean[df_clean['items_user_id'].str.lower() == User_id.lower()]
        if df_user.empty:
            raise HTTPException(status_code=404, detail=f"No se encontraron datos para el usuario {User_id}")

        total_spent = df_user['price'].sum()
        percent_recommendations = (df_user['recommend'].mean() * 100) if 'recommend' in df_user.columns else 0
        total_items = len(df_user)

        response = {
            "Usuario": User_id,
            "Dinero gastado": f"{total_spent:.2f} USD",
            "% de recomendación": f"{percent_recommendations:.2f}%",
            "Cantidad de ítems": str(total_items)
        }
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")












    