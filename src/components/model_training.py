import os,sys 

from src.logger import logging as lg
from src.exception import SketchtocodeException

from src.entity.artifact_entity import ModelTrainerArtifact, DataIngestionArtifact
from src.entity.config_entity import ModelTrainerConfig


class ModelTrainer:

    def __init__(self, data_ingestion_artifact: DataIngestionArtifact ):

        self.data_ingestion_artifact = data_ingestion_artifact
        

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
            pass 
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
            pass 
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
            pass 
        except Exception as e:
            raise SketchtocodeException(e,sys)