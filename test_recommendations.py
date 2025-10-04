#!/usr/bin/env python3
"""
Script para probar el endpoint de recomendaciones y encontrar IDs válidos
"""
import pandas as pd
import gzip

def get_sample_game_ids():
    """Obtiene una muestra de IDs de juegos válidos del dataset"""
    try:
        with gzip.open('combined_data.json.gz', 'rt', encoding='utf-8') as f:
            df = pd.read_json(f, lines=True)
        
        # Filtrar juegos que tengan información completa
        valid_games = df[
            (df['id'].notna()) & 
            (df['developer'].notna()) & 
            (df['genres'].notna())
        ].copy()
        
        # Obtener una muestra de IDs únicos
        unique_ids = valid_games['id'].unique()[:20]
        
        print("=== IDs DE JUEGOS DISPONIBLES PARA RECOMENDACIONES ===\n")
        
        for game_id in unique_ids:
            game_info = valid_games[valid_games['id'] == game_id].iloc[0]
            developer = game_info['developer']
            genres = game_info['genres']
            
            print(f"ID: {int(game_id)}")
            print(f"Desarrollador: {developer}")
            print(f"Géneros: {genres}")
            print("-" * 50)
        
        print(f"\n=== INSTRUCCIONES DE USO ===")
        print(f"Para usar el endpoint de recomendaciones, utiliza cualquiera de estos IDs:")
        print(f"Ejemplo: GET /recomendacion_juego/{int(unique_ids[0])}")
        print(f"\nEjemplos de URLs completas:")
        for i in range(min(5, len(unique_ids))):
            print(f"http://127.0.0.1:8000/recomendacion_juego/{int(unique_ids[i])}")
        
        return unique_ids
        
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
        return []

if __name__ == "__main__":
    get_sample_game_ids()
