# PROYECTO INDIVIDUAL No 1 - MACHINE LEARNING OPERATIONS

## Multinacional de Video Juegos Steam Games

![Steam Games Animated](steam_games_animated.gif)



## Introducción

Este proyecto abarca desde el análisis exploratorio de datos (EDA) hasta el despliegue de una API y la creación de un modelo de recomendación. El proceso incluye:

1. **Exploración y limpieza de datos (ETL)**
2. **Desarrollo de un modelo de recomendación utilizando técnicas de machine learning**
3. **Despliegue de la API en Render**

## Librerías Utilizadas

![Tech Stack Animated](tech_stack_animated.gif)

## Enlaces Importantes

- **API Desplegada en Render:** [https://jorge-enrique-caicedo.onrender.com/docs](https://jorge-enrique-caicedo.onrender.com/docs)
- **Video Explicativo:** [Ver en YouTube](https://youtu.be/QZ5kIKQmvoA) 🎬

## Desarrollo

### Exploración, Transformación y Carga (ETL)

Se utilizaron tres datasets proporcionados:

1. **steam_games:**
   - Descompresión y carga del archivo `.gz`
   - Extracción y limpieza de columnas
   - Desanidamiento de la columna 'genres'
   - Exportación del dataset limpio en formato JSON

2. **user_reviews:**
   - Descompresión y carga del archivo `.gz`
   - Limpieza y desanidamiento de columnas
   - Creación de la columna `sentiment_analysis`
   - Exportación del dataset limpio en formato JSON

3. **user_items:**
   - Desanidamiento y limpieza de columnas
   - Exportación del dataset limpio

### Funciones Desarrolladas

1. **developer(desarrollador: str):** Devuelve cantidad de items y porcentaje de contenido Free por año según la empresa desarrolladora.
2. **userdata(User_id: str):** Devuelve cantidad de dinero gastado por el usuario, porcentaje de recomendación y cantidad de items.
3. **user_for_genre(genre: str):** Devuelve el usuario con más horas acumuladas para el género dado.
4. **best_developer_year(año: int):** Top 3 de desarrolladores con juegos más recomendados por año.
5. **developer_reviews_analysis(desarrolladora: str):** Análisis de sentimiento de reseñas por desarrollador.
6. **recommend_games_route(game_name: str):** Retorna 5 juegos recomendados basado en el nombre del juego.

## Conclusiones

El proyecto demostró la capacidad de integrar múltiples técnicas de machine learning y procesos de ETL para crear una solución completa de recomendación y despliegue de APIs.

## Video Explicativo

[![Video Explicativo del Proyecto](video_explicativo_preview.png)](https://youtu.be/QZ5kIKQmvoA)

**Haz clic en la imagen para ver el video completo en YouTube**

## Estructura del Repositorio
 
-  Assets: sirve para almacenar y organizar los archivos multimedia y otros recursos necesarios.
-  Datasets: Archivos necesarios donde consultará nuestro codigo principal.
-  Visual Studio Code: utilizado para la exploración y desarrollo.
-  gitignore: Esto ayuda a mantener limpio el historial de versiones y evita incluir archivos innecesarios o 
   sensibles en el repositorio.
-  main.py: Código principal del proyecto para la API.
-  Readme: Sirve como una guía rápida para comprender el proyecto y contribuir eficientemente.
-  requirements.txt: Librerias necesarias para que el modelo funcione en render.

## Alumno de HENRY
## - Jorge Enrique Caicedo Riascos
