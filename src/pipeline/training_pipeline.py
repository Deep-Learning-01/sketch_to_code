from src.training_components.data_ingestion import DataIngestion
from src.training_components.model_training import ModelTrainer 
from src.training_components.model_evaluation import ModelEvaluation
from src.training_components.model_pusher import ModelPusher

from src.entity.training_entity.artifact_entity import (DataIngestionArtifact,
                                        ModelTrainerArtifact,
                                        ModelEvaluationArtifact,
                                        ModelPusherArtifact)


from src.entity.training_entity.config_entity import (DataIngestionConfig,
                                        ModelTrainerConfig,
                                        ModelEvaluationConfig,
                                        ModelPusherConfig)

from src.exception import SketchtocodeException
import sys



class TrainingPipeline:

    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.model_trainer_config = ModelTrainerConfig()
        self.model_evaluation_config = ModelEvaluationConfig()
        self.model_pusher_config = ModelPusherConfig()

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            return data_ingestion_artifact

        except Exception as e:
            raise SketchtocodeException(e,sys)



    def start_model_trainer(self,
                            data_ingestion_artifact: DataIngestionArtifact) -> ModelTrainerArtifact:
        try:
            model_trainer = ModelTrainer(model_trainer_config= self.model_trainer_config,
            data_ingestion_artifact= data_ingestion_artifact)

            model_trainer_artifact = model_trainer.initiate_model_trainer()
            return model_trainer_artifact

        except Exception as e:
            raise SketchtocodeException(e,sys)



    def start_model_evaluation(self,
                                data_ingestion_artifact: DataIngestionArtifact,
                                model_trainer_artifact: ModelTrainerArtifact) -> ModelEvaluationArtifact:
        try:
            model_evaluation = ModelEvaluation(model_evaluation_config= self.model_evaluation_config,
            data_ingestion_artifact= data_ingestion_artifact,
            model_trainer_artifact= model_trainer_artifact)
            model_evaluation_artifact = model_evaluation.initiate_model_evaluation()
            return model_evaluation_artifact

        except Exception as e:
            raise SketchtocodeException(e,sys)
            

    def start_model_pusher(self,
                            model_evaluation_artifact: ModelEvaluationArtifact,
                            model_trainer_artifact: ModelTrainerArtifact) -> ModelPusherArtifact:
        
        try:
            model_pusher = ModelPusher(model_pusher_config= self.model_pusher_config,
            
                                    model_trainer_artifact= model_trainer_artifact,
                                    model_evaluation_artifact= model_evaluation_artifact)

            model_pusher.initiate_model_pusher()
            

        except Exception as e:
            raise SketchtocodeException(e,sys)



    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            print(f'{"="*10}> Data ingestion completed {"="*10}> \n')
            model_trainer_artifact = self.start_model_trainer(data_ingestion_artifact= data_ingestion_artifact)
            print(f'{"="*10}>Model Trainer completed {"="*10}> \n')
            model_evaluation_artifact = self.start_model_evaluation(data_ingestion_artifact= data_ingestion_artifact,
                                                                    model_trainer_artifact=model_trainer_artifact)

            print(f'{"="*10}>Model Evaluation completed {"="*10}> \n')

            self.start_model_pusher(model_trainer_artifact=model_trainer_artifact,
                                    model_evaluation_artifact=model_evaluation_artifact)

            print(f'{"="*10}>Model Pusher completed {"="*10}> \n')


        except Exception as e:
            raise SketchtocodeException(e,sys)

