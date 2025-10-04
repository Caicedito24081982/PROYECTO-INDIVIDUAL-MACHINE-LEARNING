import pandas as pd
from app.core.data_handler import load_data

async def get_developer_stats(developer_name: str) -> dict:
    df_clean = load_data()
    if df_clean.empty:
        return {"error": "No se pudieron cargar los datos"}

    df_filtered = df_clean[df_clean["developer"].str.lower() == developer_name.lower()].copy()
    if df_filtered.empty:
        return {"error": f"No se encontraron datos para el desarrollador {developer_name}"}

    df_filtered["release_date"] = pd.to_datetime(df_filtered["release_date"], errors="coerce")
    df_filtered["year"] = df_filtered["release_date"].dt.year

    df_summary = df_filtered.groupby("year").apply(lambda x: {
        "Cantidad de Items": len(x),
        "Contenido Free": f"{(x['price'] == 0).mean() * 100:.2f}%"
    }).reset_index(name="Estadisticas")

    return {
        "Desarrollador": developer_name,
        "Estadísticas por año": df_summary.to_dict(orient="records")
    }

