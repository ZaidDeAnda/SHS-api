import numpy as np
import os
import requests
import json
from models import models
import random
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

model=2

GOOD_DATA_PATH="./datos_prueba_api/good/"
BAD_DATA_PATH="./datos_prueba_api/bad/"

GOOD_DATA_FILES = [GOOD_DATA_PATH + X for X in os.listdir(GOOD_DATA_PATH)]
BAD_DATA_FILES = [BAD_DATA_PATH + X for X in os.listdir(BAD_DATA_PATH)]

good_or_bad=random.randint(0,1)

if good_or_bad == 1:
    file_number=len(GOOD_DATA_FILES)
    name="good"
    file=GOOD_DATA_FILES[random.randint(0,file_number-1)]
else:
    name="bad"
    file_number=len(BAD_DATA_FILES)
    file=BAD_DATA_FILES[random.randint(0,file_number-1)]

data=np.genfromtxt(file, delimiter="\n")
data=data.tolist()

model=str(model)
url="http://localhost:6000/predict/"+model

data_json={
     "data":data
}

print(f"Se mandó un archivo de la carpeta {name}")

res = requests.post(url, json=data_json)
