from flask import Flask
from flask import request
from flask import jsonify
import numpy as np

from utils.models import load_model_folder
from utils.config_loader import load_config


meta = load_config()
models = load_model_folder(meta['models_folder'])

app = Flask(__name__)


@app.route('/')
def hello_world():
    """Test route."""

    response = {
        'message': 'Hello World!'
    }

    return jsonify(response), 200


@app.route('/predict/<int:modelo_id>', methods=['POST'])
def predict(modelo_id):
    """Predict route."""

    if modelo_id not in models.keys():
        return jsonify({'message': 'Modelo não encontrado'}), 404
    
    model = models[modelo_id]

    data = request.json['data']
    prediction = model.predict(np.reshape(data, (1, 1800)))
    
    response = {
        'prediction': float(prediction[0][0])
    }

    return jsonify(response), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)