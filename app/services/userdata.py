from typing import Dict
from app.core.data_handler import load_data
import pandas as pd

async def get_userdata(user_id: str) -> Dict[str, str]:
    """
    Devuelve información sobre un usuario específico
    """
    df = load_data()
    
    # Asegurarse de que 'price' sea numérico
    df['price'] = pd.to_numeric(df['price'], errors='coerce').fillna(0)
    
    df_user = df[df['items_user_id'].str.lower() == user_id.lower()]
    if df_user.empty:
        raise ValueError(f"No se encontraron datos para el usuario {user_id}")
    
    total_spent = df_user['price'].sum()
    percent_recommendations = (df_user['recommend'].mean() * 100) if 'recommend' in df_user.columns else 0
    total_items = len(df_user)
    
    response = {
        "Usuario": user_id,
        "Dinero gastado": f"{total_spent:.2f} USD",
        "% de recomendación": f"{percent_recommendations:.2f}%",
        "Cantidad de ítems": str(total_items)
    }
    return response
