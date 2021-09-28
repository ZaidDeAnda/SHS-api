import tensorflow as tf
from tensorflow import keras
import numpy as np
from flask.json import jsonify
from flask import request
import urllib

models = [
    tf.keras.models.load_model('./Modelos SHS/modelo' + str(i))
    for i in range(1, 6)
]

def url_to_data(url):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format
    with urllib.request.urlopen(url) as link:
        resp = link.read()
    # return the image
    return resp