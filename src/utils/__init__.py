import yaml
from src.constant.training_pipeline import *
from src.constant.prediction_pipeline import *
from src.exception import SketchtocodeException

from detectron2.config.config import CfgNode
import os,sys
import os,sys
import subprocess
from box import ConfigBox


def read_yaml_file(filepath: str) -> dict:
        try:
            with open(filepath, "rb") as yaml_file:
                return yaml.safe_load(yaml_file)

        except Exception as e:
            raise SketchtocodeException(e, sys)


def get_training_model_config_attribute():
    try:
        model_config_file_path = os.path.join(ROOT_DIR,CONFIG_STORE_DIR, 
                                                MODEL_TRAINER_TEXT_DET_MODEL_YAML_FILE_DIR_NAME,
                                                MODEL_CONFIG_FILE_NAME)
        model_config_yaml = read_yaml_file(model_config_file_path)
        model_config_attributes = ConfigBox(model_config_yaml)
        return model_config_attributes
    except Exception as e:
        raise SketchtocodeException(e, sys)


def get_yaml_file_attributes(yaml_file_path):
    try:
        yaml_file = read_yaml_file(yaml_file_path)
        yaml_attributes = ConfigBox(yaml_file)
        return yaml_attributes
        
    except Exception as e:
        raise SketchtocodeException(e, sys)

def get_prediction_model_config_attribute():
    try:
        model_config_file_path = os.path.join(ROOT_DIR,CONFIG_STORE_DIR, 
                                                MODEL_PREDICTOR_MODEL_YAML_FILE_DIR_NAME,
                                                MODEL_PREDICTOR_MODEL_YAML_FILE_NAME)
        model_config_yaml = read_yaml_file(model_config_file_path)
        model_config_attributes = ConfigBox(model_config_yaml)
        return model_config_attributes

    except Exception as e:
        raise SketchtocodeException(e, sys)


def save_model_config_to_yaml_file(model_config:CfgNode, model_config_file_path:str):
    try:
        os.makedirs( os.path.dirname(model_config_file_path), exist_ok=True)
        with open(model_config_file_path, "w") as yaml_file:
            yaml_file.write(model_config.dump())
    except Exception as e:
        raise SketchtocodeException(e, sys)

def is_model_present_in_s3(model_path):
    try:
        
        command = f"""aws s3api list-objects-v2 --bucket {TRAINING_BUCKET_NAME} --query "contains(Contents[].Key, '{model_path}')" """
          
        output = subprocess.check_output(command, shell=True)

        output = output.decode('utf-8').rstrip()

        output = True if output=='true' else False

        return output
        
    except Exception as e:
        raise SketchtocodeException(e, sys)






