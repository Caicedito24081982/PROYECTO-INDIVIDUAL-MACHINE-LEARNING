# 🚀 Guía Paso a Paso: Cómo Usar el Endpoint de Recomendaciones

## Paso 1: Preparar el Entorno

### 1.1 Abrir Terminal/Consola
- En Windows: Presiona `Win + R`, escribe `cmd` y presiona Enter
- En Mac/Linux: Abre Terminal

### 1.2 Navegar al Directorio del Proyecto
```bash
cd ruta/a/tu/PROYECTO-INDIVIDUAL-MACHINE-LEARNING
```

### 1.3 Activar el Entorno Virtual (si tienes uno)
```bash
# En Windows
venv\Scripts\activate

# En Mac/Linux
source venv/bin/activate
```

### 1.4 Instalar Dependencias
```bash
pip install -r requirements.txt
```

---

## Paso 2: Iniciar la API

### 2.1 Ejecutar el Comando para Iniciar FastAPI
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 2.2 Verificar que la API Esté Funcionando
Deberías ver algo como esto en tu terminal:
```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [12345] using StatReload
INFO:     Started server process [12346]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

---

## Paso 3: Probar la API

### 3.1 Abrir tu Navegador Web
Ve a: `http://127.0.0.1:8000/docs`

Esto te mostrará la documentación interactiva de Swagger UI.

### 3.2 Usar el Endpoint Directamente en el Navegador

**Opción A: Desde el Navegador**
Copia y pega cualquiera de estas URLs en tu navegador:

```
http://127.0.0.1:8000/recomendacion_juego/761140
http://127.0.0.1:8000/recomendacion_juego/643980
http://127.0.0.1:8000/recomendacion_juego/670290
```

**Opción B: Desde Swagger UI**
1. Ve a `http://127.0.0.1:8000/docs`
2. Busca el endpoint `/recomendacion_juego/{product_id}`
3. Haz clic en "Try it out"
4. En el campo `product_id`, ingresa: `761140`
5. Haz clic en "Execute"

---

## Paso 4: Entender la Respuesta

### 4.1 Respuesta Exitosa
Si todo funciona correctamente, verás algo como:
```json
[
  {
    "id": 643980,
    "title": null
  },
  {
    "id": 670290,
    "title": null
  },
  {
    "id": 767400,
    "title": null
  },
  {
    "id": 772540,
    "title": null
  },
  {
    "id": 774276,
    "title": null
  }
]
```

**Nota:** Los títulos aparecen como `null` porque tu dataset no incluye nombres de juegos, solo IDs.

### 4.2 Posibles Errores y Soluciones

**Error 404: "ID de producto no encontrado"**
- **Causa:** El ID que usaste no existe en el dataset
- **Solución:** Usa uno de los IDs válidos que te proporcioné

**Error 500: "Error interno del servidor"**
- **Causa:** Problema con la carga de datos o el modelo
- **Solución:** Verifica que el archivo `combined_data.json.gz` esté en el directorio raíz

---

## Paso 5: Probar con Diferentes Herramientas

### 5.1 Con cURL (Línea de Comandos)
```bash
curl -X GET "http://127.0.0.1:8000/recomendacion_juego/761140"
```

### 5.2 Con Postman
1. Abre Postman
2. Crea una nueva petición GET
3. URL: `http://127.0.0.1:8000/recomendacion_juego/761140`
4. Haz clic en "Send"

### 5.3 Con Python (requests)
```python
import requests

response = requests.get("http://127.0.0.1:8000/recomendacion_juego/761140")
print(response.json())
```

---

## 📋 Lista de IDs Válidos para Probar

Usa cualquiera de estos IDs en lugar de `{product_id}`:

| ID | Desarrollador | Géneros |
|---|---|---|
| 761140 | Kotoshiro | Action, Casual, Indie, Simulation, Strategy |
| 643980 | Secret Level SRL | Free to Play, Indie, RPG, Strategy |
| 670290 | Poolians.com | Casual, Free to Play, Indie, Simulation, Sports |
| 767400 | 彼岸领域 | Action, Adventure, Casual |
| 772540 | Trickjump Games Ltd | Action, Adventure, Simulation |
| 774276 | Poppermost Productions | Free to Play, Indie, Simulation, Sports |
| 768800 | RewindApp | Casual, Indie, Racing, Simulation |
| 770380 | Stegalosaurus Game Development | Action, Adventure, Casual, Indie, RPG |

---

## 🔧 Solución de Problemas Comunes

### Problema: "ModuleNotFoundError"
**Solución:**
```bash
pip install fastapi uvicorn pandas scikit-learn
```

### Problema: "Port already in use"
**Solución:** Cambia el puerto:
```bash
uvicorn app.main:app --reload --port 8001
```
Luego usa: `http://127.0.0.1:8001/recomendacion_juego/761140`

### Problema: La API no responde
**Solución:**
1. Verifica que el archivo `combined_data.json.gz` esté presente
2. Revisa que no haya errores en la terminal
3. Reinicia la API con Ctrl+C y vuelve a ejecutar el comando

---

## ✅ Verificación Final

Para confirmar que todo funciona:

1. **Terminal muestra:** "Application startup complete"
2. **Navegador en** `http://127.0.0.1:8000/docs` **muestra:** Documentación de Swagger
3. **URL** `http://127.0.0.1:8000/recomendacion_juego/761140` **devuelve:** Lista JSON con 5 recomendaciones

¡Listo! Tu endpoint de recomendaciones está funcionando correctamente.
