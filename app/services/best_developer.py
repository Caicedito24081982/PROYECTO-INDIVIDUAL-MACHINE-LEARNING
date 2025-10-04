from typing import List, Dict
from app.core.data_handler import load_data
import pandas as pd

async def get_best_developer_year(year: int) -> List[Dict[str, str]]:
    """
    Devuelve los top 3 desarrolladores con más juegos recomendados en un año específico
    """
    df = load_data()
    
    # Asegurarse de que 'release_date' es de tipo datetime
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
    
    # Filtrar filas donde 'release_date' es NaT (Not a Time)
    df = df.dropna(subset=['release_date'])
    
    # Filtrar por año y recomendaciones positivas
    df_filtered = df[
        (df['release_date'].dt.year == year) &
        (df['recommend'] == True)
    ]
    
    if df_filtered.empty:
        return []
    
    # Agrupar por desarrollador y contar recomendaciones positivas
    df_recommendations = df_filtered.groupby('developer').size().reset_index(name='recommendations')
    top_developers = df_recommendations.nlargest(3, 'recommendations').reset_index(drop=True)
    
    # Crear la respuesta
    response = [{f"Puesto {i+1}": row['developer']} for i, row in top_developers.iterrows()]
    return response
