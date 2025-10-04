import pandas as pd
from app.core.data_handler import load_data

async def get_user_for_genre(genre: str) -> dict:
    df_clean = load_data()
    if df_clean.empty:
        return {"error": "No se pudieron cargar los datos"}

    df_filtered = df_clean[df_clean["genres"].apply(lambda x: genre in x if x is not None else False)]
    if df_filtered.empty:
        return {"error": f"No se encontraron datos para el género {genre}"}

    df_filtered["release_date"] = pd.to_datetime(df_filtered["release_date"], errors="coerce")
    df_filtered["year"] = df_filtered["release_date"].dt.year

    top_user = df_filtered.groupby("items_user_id")["playtime_forever"].sum().idxmax()

    hours_by_year = df_filtered.groupby("year")["playtime_forever"].sum().reset_index(name="Horas")
    hours_by_year = hours_by_year.sort_values("year")

    return {
        f"Usuario con más horas jugadas para Género {genre}": top_user,
        "Horas jugadas": hours_by_year.to_dict(orient="records")
    }

