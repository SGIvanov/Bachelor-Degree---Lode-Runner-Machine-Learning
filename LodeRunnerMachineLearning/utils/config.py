import json
from bunch import Bunch
import os
import time


def get_config_from_json(json_file):
    """
    Get the config from a json file
    :param json_file:
    :return: config(namespace) or config(dictionary)
    """
    # parse the configurations from the config json file provided
    with open(json_file, 'r') as config_file:
        config_dict = json.load(config_file)

    # convert the dictionary to a namespace using bunch lib
    config = Bunch(config_dict)

    return config, config_dict


def process_config(json_file):
    """
    Add to the config file the paths for logs and checkpoints.
    :param json_file:Configuration File
    :return:New Bunch Config
    """
    config, _ = get_config_from_json(json_file)
    config.tensorboard_log_dir = os.path.join("experiments", time.strftime("%Y-%m-%d-%H-%M/",time.localtime()), config.exp_name, "logs/")
    config.checkpoint_dir = os.path.join("experiments", time.strftime("%Y-%m-%d-%H-%M/",time.localtime()), config.exp_name, "checkpoints/")
    return config
