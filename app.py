from flask import Flask, request
from flask.json import jsonify
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

app = Flask(__name__)

from models import models

@app.route("/predict/<int:modelo>", methods=['POST'])
def predict(modelo):
    """ Le pasas un json cuyo único elemento es la lista de los valores del ECG
    """
    model=models[modelo]
    if model:
        data=request.json["data"]
        prediction=model.predict(np.reshape(data, (1,1800))) 
    print(prediction[0][0])
    return str(prediction[0][0])

if __name__ == '__main__':
    app.run(debug=True, port=6000)