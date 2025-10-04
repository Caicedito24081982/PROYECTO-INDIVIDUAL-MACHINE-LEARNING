#!/usr/bin/env python3
"""
Script para probar rápidamente el endpoint de recomendaciones
"""
import requests
import time
import subprocess
import sys
from threading import Thread

def start_server():
    """Inicia el servidor FastAPI"""
    subprocess.run([
        "uvicorn", "app.main:app", 
        "--host", "0.0.0.0", 
        "--port", "8000"
    ])

def test_endpoint():
    """Prueba el endpoint de recomendaciones"""
    print("🚀 Esperando que el servidor se inicie...")
    time.sleep(3)
    
    test_ids = [761140, 643980, 670290]
    
    for test_id in test_ids:
        try:
            print(f"\n🎮 Probando con ID: {test_id}")
            url = f"http://127.0.0.1:8000/recomendacion_juego/{test_id}"
            
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                print(f"✅ ¡Éxito! Recibidas {len(data)} recomendaciones:")
                for i, game in enumerate(data, 1):
                    print(f"   {i}. ID: {game.get('id', 'N/A')}")
            else:
                print(f"❌ Error {response.status_code}: {response.text}")
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Error de conexión: {e}")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
    
    print(f"\n🌐 URLs para probar en tu navegador:")
    for test_id in test_ids:
        print(f"   http://127.0.0.1:8000/recomendacion_juego/{test_id}")
    
    print(f"\n📚 Documentación interactiva:")
    print(f"   http://127.0.0.1:8000/docs")

if __name__ == "__main__":
    print("🔧 Iniciando prueba del endpoint de recomendaciones...")
    
    # Iniciar servidor en un hilo separado
    server_thread = Thread(target=start_server, daemon=True)
    server_thread.start()
    
    # Probar el endpoint
    test_endpoint()
    
    print(f"\n⚠️  El servidor sigue corriendo. Presiona Ctrl+C para detenerlo.")
    print(f"   Puedes seguir probando los endpoints manualmente.")
    
    try:
        # Mantener el script corriendo
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n👋 ¡Servidor detenido!")
        sys.exit(0)
