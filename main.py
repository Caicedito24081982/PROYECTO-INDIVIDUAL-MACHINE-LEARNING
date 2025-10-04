"""
Punto de entrada principal para Render
Importa la aplicación modular desde app/main.py
"""

from app.main import app

# Esto permite que Render use este archivo como punto de entrada
# mientras mantenemos la estructura modular en app/
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
