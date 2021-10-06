import tensorflow as tf
import numpy as np

from glob import glob
from pprint import pprint


def model_loader(model_path):
    """Loads the model from the checkpoint file.

    Parameters
    ----------
    model_path : str
        Path to the checkpoint file.
    
    Returns
    -------
    model : tf.keras.Model
        The loaded model.
    """

    model = tf.keras.models.load_model(model_path)

    return model


def load_model_folder(model_folder):
    """Loads models from the checkpoint files in the model folder.

    Parameters
    ----------
    model_folder : str
        Path to the model folder.
    
    Returns
    -------
    models : dict
        Dictionary of models.
    """

    models = {}

    models_path = sorted(glob(model_folder + '/*'))

    for model in models_path:
        model_id = model.split('/')[-1]
        models[int(model_id)] = model_loader(model)
    
    return models


if __name__ == '__main__':
    models = load_model_folder('./models')
    pprint(models)