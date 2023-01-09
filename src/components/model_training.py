import os,sys 

from src.logger import logging as lg
from src.exception import SketchtocodeException

from src.entity.artifact_entity import ModelTrainerArtifact, DataIngestionArtifact
from src.entity.config_entity import ModelTrainerConfig
from src.utils import get_model_config_attribute, save_model_config_to_yaml_file

import torch, torchvision

import detectron2
from detectron2.utils.logger import setup_logger
setup_logger()

# import some common libraries
import numpy as np
import os
# from google.colab.patches import cv2_imshow

# import some common detectron2 utilities
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog, DatasetCatalog
from detectron2.data.datasets import register_coco_instances

from detectron2 import model_zoo
from detectron2.engine import DefaultTrainer, DefaultPredictor
from detectron2.config import get_cfg




class ModelTrainer:

    def __init__(self, data_ingestion_artifact: DataIngestionArtifact ):

        self.data_ingestion_artifact = data_ingestion_artifact
        self.model_trainer_config = ModelTrainerConfig()
        self.model_config = get_model_config_attribute()
        
        

    def train_object_detection_model(self):
        """
            Method Name :   train_object_detection_model
            Description :   This method initiates the training of object detection model and saves the model
            Output      :   NA
            On Failure  :   Write an exception log and then raise an exception

            Version     :   1.2
            Revisions   :   moved setup to cloud
        """
        try:
            obj_det_model_config = self.model_config.MODEL_CONFIG.OBJECT_DETECTION_MODEL.CONFIG

            train_coco_ins_name = self.model_trainer_config.obj_detection_train_coco_ins_name
            
            register_coco_instances(name= train_coco_ins_name,
                                    metadata={},
                                    json_file= self.data_ingestion_artifact.obj_detection_coco_train_annot_path,
                                    image_root= self.data_ingestion_artifact.obj_detection_training_data_folder_path )
            
       


            config = get_cfg()
            config.merge_from_file(model_zoo.get_config_file(self.model_trainer_config.obj_detection_model_yaml_file_path))

            config.DATASETS.TRAIN = (train_coco_ins_name,)
            config.DATASETS.TEST = ()
            config.DATALOADER.NUM_WORKERS = obj_det_model_config.DATALOADER.NUM_WORKERS
            config.MODEL.WEIGHTS = model_zoo.get_checkpoint_url(self.model_trainer_config.obj_detection_model_yaml_file_path)
      
            config.SOLVER.IMS_PER_BATCH = obj_det_model_config.SOLVER.IMS_PER_BATCH
            config.SOLVER.BASE_LR = obj_det_model_config.SOLVER.BASE_LR
            config.SOLVER.MAX_ITER = obj_det_model_config.SOLVER.MAX_ITER
            config.MODEL.ROI_HEADS.BATCH_SIZE_PER_IMAGE = obj_det_model_config.MODEL.ROI_HEADS.BATCH_SIZE_PER_IMAGE
            config.MODEL.ROI_HEADS.NUM_CLASSES = obj_det_model_config.MODEL.ROI_HEADS.NUM_CLASSES
            config.OUTPUT_DIR = self.model_trainer_config.obj_detection_model_output_dir

            config.INPUT.MAX_SIZE_TRAIN = 1333
            config.INPUT.MIN_SIZE_TRAIN = (1280,)
            config.MAX_SIZE_TEST: 1333
            config.MIN_SIZE_TEST: 1280

            os.makedirs(config.OUTPUT_DIR, exist_ok=True)

            trainer = DefaultTrainer(config)
            trainer.resume_or_load(resume=False)
            trainer.train()

            lg.info("object detection training completed")

            save_model_config_to_yaml_file(model_config= config,
            model_config_file_path= self.model_trainer_config.obj_detection_training_config_file_path)


        except Exception as e:
            raise SketchtocodeException(e,sys)

    def train_text_detection_model(self):
        """
            Method Name :   train_text_detection_model
            Description :   This method initiates the training of text detection model and saves the model
            Output      :   NA
            On Failure  :   Write an exception log and then raise an exception

            Version     :   1.2
            Revisions   :   moved setup to cloud
        """
        try:
            text_det_model_config = self.model_config.MODEL_CONFIG.TEXT_DETECTION_MODEL.CONFIG

            train_coco_ins_name = self.model_trainer_config.text_detection_train_coco_ins_name
            # test_coco_ins_name = self.model_trainer_config.obj_detection_test_coco_ins_name
            
            register_coco_instances(name= train_coco_ins_name,
                                    metadata={},
                                    json_file= self.data_ingestion_artifact.text_detection_coco_train_annot_path,
                                    image_root= self.data_ingestion_artifact.text_detection_training_data_folder_path )
            
           

            

           

            config = get_cfg()
            config.merge_from_file(self.model_trainer_config.text_detection_model_yaml_file_path)

            config.DATASETS.TRAIN = (train_coco_ins_name,)
       
            config.OUTPUT_DIR = self.model_trainer_config.text_detection_model_output_dir

            os.makedirs(config.OUTPUT_DIR, exist_ok=True)

            trainer = DefaultTrainer(config)
            trainer.resume_or_load(resume=False)
            trainer.train()

            lg.info("Text detection training completed")

            save_model_config_to_yaml_file(model_config= config,
            model_config_file_path= self.model_trainer_config.text_detection_training_config_file_path)


        except Exception as e:
            raise SketchtocodeException(e,sys)

    
    def initiate_model_trainer(self) -> ModelTrainerArtifact:
        """
            Method Name :   initiate_model_trainer
            Description :   This method initiates model training component of the training pipeline.
            Output      :   NA
            On Failure  :   Write an exception log and then raise an exception

            Version     :   1.2
            Revisions   :   moved setup to cloud
        """
        try:
            lg.info("Entered into model training component of the training pipeline")

            self.train_object_detection_model()
            self.train_text_detection_model() 

            lg.info("Model training completed")

            model_trainer_artifact = ModelTrainerArtifact(
                obj_detection_trained_model_file_path= self.model_trainer_config.obj_detection_saved_model_path,
                text_detection_trained_model_file_path= self.model_trainer_config.text_detection_saved_model_path,
                obj_detection_trained_model_config_file_path= self.model_trainer_config.obj_detection_training_config_file_path,
                text_detection_trained_model_config_file_path= self.model_trainer_config.text_detection_training_config_file_path 

            )

            lg.info("Exited the model training component of the training pipeline.")
            return model_trainer_artifact
        except Exception as e:
            raise SketchtocodeException(e,sys)