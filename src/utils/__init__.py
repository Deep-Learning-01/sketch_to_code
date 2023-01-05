import yaml
from src.constant.training_pipeline import *
from src.exception import SketchtocodeException
import os,sys
from box import ConfigBox


def read_yaml_file(filepath: str) -> dict:
        try:
            with open(filepath, "rb") as yaml_file:
                return yaml.safe_load(yaml_file)

        except Exception as e:
            raise SketchtocodeException(e, sys)


def get_model_config_attribute():
    try:
        model_config_file_path = MODEL_CONFIG_FILE_PATH
        model_config_yaml = read_yaml_file(model_config_file_path)
        model_config_attributes = ConfigBox(model_config_yaml)
        return model_config_attributes
    except Exception as e:
        raise SketchtocodeException(e, sys)




