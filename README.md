# Prueba de API para SHS

Primero crear un entorno virtual con

`python3 -m venv venv`

Luego, instalar los requisitos con

`pip install -r requirements.txt`

Para levantar la api, correr 

`python3 app.py`

Luego para mandar un ECG de la muestra seleccionada, correr 

`json_generator.py`

que seleccionará un dato al azar de cualquiera de las dos categorías de datos.

Para cambiar el modelo que realiza la predicción en la API, basta con cambiar

`model=2`

que está dentro de json_generator.py, por cualquier número del 0 al 2, siendo estos los modelos disponibles 
