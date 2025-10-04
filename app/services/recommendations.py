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

    df_games["genres"] = df_games["genres"].apply(lambda x: " ".join(x) if x else "")
    df_games["developer"] = df_games["developer"].fillna("")
    df_games["combined_features"] = df_games["genres"] + " " + df_games["developer"]
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
    recommended_games = df_games.iloc[game_indices][["id", "title"]].to_dict(orient="records")

    return recommended_games

