import os,sys 

from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2 import model_zoo

import numpy as np

from src.exception import SketchtocodeException
from src.logger import logging as lg  
from src.entity.config_entity import ModelTrainerConfig
from src.utils import get_prediction_model_config_attribute



class ImageDetection:

    def __init__(self,
                model_file_path:str):

        self.model_trainer_config = ModelTrainerConfig()
        self.model_prediction_config = get_prediction_model_config_attribute()
        

    def get_config(self):
        try:
            config = get_cfg()
        except Exception as e:
            raise SketchtocodeException(e, sys)

    def build_predictor_model(self):
        try:
            model_config_file = self.model_trainer_config.obj_detection_model_yaml_file_path
            
        except Exception as e:
            raise SketchtocodeException(e,sys)