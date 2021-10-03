# Prueba de API para SHS

Primero crear un entorno virtual con

`python3 -m venv venv`

Luego, instalar los requisitos con

`pip install -r requirements.txt`

Descargar la carpeta de modelos de [AQUI](https://drive.google.com/drive/folders/1IKw8qrmYGHUj6GkiA7MI7nRCdyEILxxp?usp=sharing) y colocarla en la carpeta raiz del repositorio. 

Para levantar la api, correr 

`python3 app.py`

Luego para mandar un ECG de la muestra seleccionada, correr 

`json_generator.py`

que seleccionará un dato al azar de cualquiera de las dos categorías de datos.

Para cambiar el modelo que realiza la predicción en la API, basta con cambiar

`model=2`

que está dentro de json_generator.py, por cualquier número del 0 al 5, siendo estos los modelos disponibles 

