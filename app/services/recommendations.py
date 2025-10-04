import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from app.core.data_handler import load_data

df_games = None
cosine_sim = None

def load_recommendation_model():
    global df_games, cosine_sim
    df_games = load_data()
    if df_games.empty:
        return

    # Convertir géneros de string a lista si es necesario
    def parse_genres(x):
        if x is None:
            return []
        if isinstance(x, str):
            # Si es un string que parece una lista, evaluarlo
            if x.startswith('[') and x.endswith(']'):
                try:
                    import ast
                    return ast.literal_eval(x)
                except:
                    return []
            else:
                return [x]  # Si es un string simple, convertir a lista
        return x if isinstance(x, list) else []

    df_games["genres_list"] = df_games["genres"].apply(parse_genres)
    df_games["genres_str"] = df_games["genres_list"].apply(lambda x: " ".join(x) if x else "")
    df_games["developer"] = df_games["developer"].fillna("")
    df_games["combined_features"] = df_games["genres_str"] + " " + df_games["developer"]
    df_games["combined_features"] = df_games["combined_features"].fillna("")

    vectorizer = TfidfVectorizer(stop_words="english")
    feature_vectors = vectorizer.fit_transform(df_games["combined_features"])
    cosine_sim = cosine_similarity(feature_vectors)

async def get_game_recommendation(product_id: int) -> list:
    global cosine_sim, df_games
    if cosine_sim is None or df_games is None:
        load_recommendation_model()

    if product_id not in df_games["id"].values:
        return [{"error": "ID de producto no encontrado."}]

    idx = df_games.index[df_games["id"] == product_id].tolist()[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]
    game_indices = [i[0] for i in sim_scores]
    
    # Crear recomendaciones con información disponible
    recommended_games = []
    for idx in game_indices:
        game_data = df_games.iloc[idx]
        recommended_games.append({
            "id": int(game_data["id"]),
            "developer": game_data["developer"] if pd.notna(game_data["developer"]) else "Unknown",
            "genres": game_data["genres_list"] if "genres_list" in game_data else []
        })

    return recommended_games

