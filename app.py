from flask import Flask, request
from flask.json import jsonify
import wget

app = Flask(__name__)

from models import models, url_to_data

@app.route("/predict/<int:modelo>", methods=['POST'])
def predict(modelo):
    """ Le pasas un json con el link del archivo a analizar, junto con el modelo elegido
    """
    model=models[modelo]
    if model:
        url=request.json["url"]
        raw_file = wget.download(url)
        #model.predict(np.reshape(data, (1,1800)))
    return jsonify({"raw_file":raw_file})

if __name__ == '__main__':
    app.run(debug=True, port=4000)