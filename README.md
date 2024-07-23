
## PROYECTO INDIVIDUAL No 1 

## -MACHINE LEARNING OPERATIONS-
                            

![image](https://github.com/Caicedito24081982/PROYECTO-INDIVIDUAL-MACHINE-LEARNING/assets/120407303/51291457-63f5-4ad0-87e6-9e5fe1646fb9)


 ##  LIBRERIAS UTILIZADAS
![image](https://github.com/Caicedito24081982/PROYECTO-INDIVIDUAL-MACHINE-LEARNING/assets/120407303/4dcafe42-a0c1-44d8-ba5c-2d3ee6dd6d8c)


                


  
   
   
   
   ## Link API desplegada en Render:  https://jorge-enrique-caicedo.onrender.com/docs#/                                                                                           Link video:  https://youtu.be/QZ5kIKQmvoA


   
  ## INTRODUCCION    

Para llevar adelante el proyecto, seguí un proceso estructurado desde el análisis exploratorio de datos (EDA) hasta el despliegue de la API y la creación del modelo de recomendación. 

Inicie explorando,analizando y limpiando los datos (ETL), identificando y creando las columnas necesarias para la creacion de las cinco funciones en FastAPI. Luego, desarrollé un modelo de recomendación utilizando técnicas de machine learning. Posterirmente documenté todo el proceso en este README de forma detallada. Finalmente, desplegué la API y modelo en Render y cree un video demostrativo del funcionamiento de los endpoints y el modelo de recomendación, siguiendo las directrices específicas del proyecto y asegurando la calidad y prolijidad de los códigos, así como la claridad en la documentación y presentación del proyecto.

## Aqui una imagen-diccionario-del Dataframe general, tres(3) archivos: 

![image](https://github.com/Caicedito24081982/PROYECTO-INDIVIDUAL-MACHINE-LEARNING/assets/120407303/1ca8ddc3-728d-4c4e-878e-0170427db54b)

### DESARROLLO

Exploración, Transformación y Carga (ETL)
A partir de los 3 dataset proporcionados (steam_games, user_reviews y user_items) referentes a la plataforma de Steam, en primera instancia se realizó el proceso de extraccion de los datos necesarios los cuales se resaltan en la anterior imagen.

ES IMPORTANTANTE RESALTAR QUE, EL ETL, EN MAYOR PROPORCION, SE EFEECTUO AL ARCHIVO DENOMINADO, combined_data.json.gz

## Archivo steam_games:

Se cargo el archivo que venia en formato '.gz', se descomprimio y se cargo a un DataFrame para poder manejar el contenido.
Se extrajo las columnas necesarias para nuestro proyecto.
Se eliminaron todas las filas en las que todas sus columnas tuvieran valores nulos.
Se extrajeron años de la columna release_date.
Se desanido la columna 'genres' ya que traia mas de un genero para un mismo juego.
Se exportó para tener el dataset limpio en un formato JSON para despues facilitar su lectura.

## Archivo user_reviews:

Se cargo el archivo que venia en formato '.gz', se descomprimio y se cargo en un DataFrame para poder manejar los datos.
Se eliminaro todas las filas en las que todas sus columnas tuvieran valores nulos.
Se desanido la columna 'reviews' que contenia diccionarios.
Se desanidaron los diccionarios que tenia en la columna reviews anteriormente creados y se creo nuevas columnas para cada dato del diccionario.
Se tomaron unicamente las columnas necesarias para nuestro proyecto.
Se creó la columna sentiment_analysis. Se hizo un analisis de sentimiento para la columna 'review' que contenia comentarios de usuarios para darle un mejor manejo.
Se exportó para tener el dataset limpio en un formato JSON para despues facilitar su lectura.

## Archivo user_items:

Se realizó un explode ya que la columna de items era una lista de diccionarios.
Se eliminaro todas las filas en las que todas sus columnas tuvieran valores nulos.
Se exportó para tener el dataset limpio.

Finalmente, se crea un dataset comprimido en formato JSON, en el que se combinan todas las columnas ya limpias y  necesarias para ser consumidas por FASTAPI. 

Despliegue para la API
Se desarrollaron las siguientes funciones, a las cuales se podrá acceder desde la API en la página Render:

.def developer( desarrollador : str ): Devuelve cantidad de items y porcentaje de contenido Free por año según empresa desarrolladora.

.def userdata( User_id : str ): Devuelve cantidad de dinero gastado por el usuario, el porcentaje de recomendación en base a reviews.recommend y cantidad de items.

.user_for_genre(genre: str):Devuelve el usuario con mas horas acumuladas para el genero dado.

.def best_developer_year( año : int ): Devuelve el top 3 de desarrolladores con juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos).

.def developer_reviews_analysis( desarrolladora : str ): Según el desarrollador, devuelve un diccionario con el nombre del desarrollador como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor positivo o negativo.

recommend_games_route(game_name: str): Dado el nombre de un juego, esta funsion retorna 5 juegos recomendados.


## Video explicativo: https://www.youtube.com/watch?v=QZ5kIKQmvoA&t=183s
