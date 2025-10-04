from typing import Dict
from app.core.data_handler import load_data

async def get_developer_reviews_analysis(desarrolladora: str) -> Dict[str, Dict[str, int]]:
    """
    Analiza las reseñas de un desarrollador específico
    """
    df = load_data()
    
    # Filtrar por desarrollador
    df_filtered = df[df['developer'].str.lower() == desarrolladora.lower()]
    if df_filtered.empty:
        return {desarrolladora: {"Negative": 0, "Positive": 0}}
    
    # Contar reseñas positivas y negativas basadas en el análisis de sentimiento
    sentiment_counts = df_filtered['sentiment_analysis'].value_counts().to_dict()
    
    # Mapear valores numéricos a texto si es necesario
    # Asumiendo: 0 = Negative, 1 = Neutral, 2 = Positive
    positive_reviews = sentiment_counts.get(2, 0)  # Valor 2 = Positive
    negative_reviews = sentiment_counts.get(0, 0)  # Valor 0 = Negative
    
    # Si los valores ya están como texto
    if "Positive" in sentiment_counts:
        positive_reviews = sentiment_counts.get("Positive", 0)
    if "Negative" in sentiment_counts:
        negative_reviews = sentiment_counts.get("Negative", 0)
    
    # Crear la respuesta ajustada al formato especificado
    response = {
        desarrolladora: {"Negative": negative_reviews, "Positive": positive_reviews}
    }
    return response
