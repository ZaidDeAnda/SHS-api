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
