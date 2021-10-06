import yaml


def load_config(config_file='config.yaml'):
    """Utility function to load email parameters.
    
    Parameters
    ----------
    config_file : str
        Path to the config file.
    Returns
    -------
    meta : dict
        A dictionary containing all the meta information about the
        API.
    """

    with open(config_file) as config:
        meta = yaml.load(config, Loader=yaml.FullLoader)

    return meta