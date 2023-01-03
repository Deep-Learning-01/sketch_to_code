import os
from src.constant.training_pipeline import *
from src.constant.prediction_pipeline import * 

from dataclasses import dataclass
from datetime import datetime

TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")


@dataclass
class TrainingPipelineConfig:
    pipeline_name: str = PIPELINE_NAME
    artifact_dir: str = os.path.join(ARTIFACT_DIR, TRAINING_ARTIFACT_DIR,TIMESTAMP)
    timestamp: str = TIMESTAMP


training_pipeline_config: TrainingPipelineConfig = TrainingPipelineConfig()


@dataclass
class DataIngestionConfig:
    data_ingestion_dir: str = os.path.join(training_pipeline_config.artifact_dir, DATA_INGESTION_DIR_NAME)    
    ingested_data_dir: str = os.path.join(data_ingestion_dir, DATA_INGESTION_INGESTED_DIR)


    object_detection_data_store_dir: str = os.path.join(ingested_data_dir, DATA_INGESTION_OBJ_DET_DIR, DATA_INGESTION_DATA_STORE_DIR )
    text_detection_data_store_dir: str = os.path.join(ingested_data_dir, DATA_INGESTION_TEXT_DET_DIR, DATA_INGESTION_DATA_STORE_DIR)
    
    training_folder_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, DATA_INGESTION_TRAIN_DIR )
    testing_folder_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, DATA_INGESTION_TEST_DIR)





@dataclass
class ModelTrainerConfig:
    model_trainer_artifact_dir: str = os.path.join(training_pipeline_config.artifact_dir, MODEL_TRAINER_ARTIFACT_DIR_NAME)
    trained_model_file_path: str = os.path.join(model_trainer_artifact_dir, MODEL_TRAINER_TRAINED_MODEL_DIR, MODEL_TRAINER_TRAINED_MODEL_NAME)
    trained_model_base_acc_score:float = MODEL_TRAINER_TRAINED_MODEL_BASE_ACC_SCORE


@dataclass
class ModelEvaluationConfig:
    model_eval_artifact_dir = os.path.join(training_pipeline_config.artifact_dir, MODEL_EVALUATION_DIR_NAME)
    s3_model_key_path: str = MODEL_EVALUATION_BEST_MODEL_NAME
    best_model_dir:str  = os.path.join(model_eval_artifact_dir, MODEL_EVALUATION_BEST_MODEL_DIR)
    best_model_path:str = os.path.join(best_model_dir, s3_model_key_path)






@dataclass
class PredictionPipelineConfig:

    model_bucket_name = TRAINING_BUCKET_NAME
    pred_artifact_dir = os.path.join(ARTIFACT_DIR ,PREDICTION_ARTIFACT_DIR,TIMESTAMP)
    pred_file_input_dir = os.path.join(pred_artifact_dir, PRED_INPUT_FILE_DIR_NAME)
    pred_model_dir = os.path.join(pred_artifact_dir, PREDICTION_MODEL_DIR_NAME)
    pred_model_full_path = os.path.join(pred_model_dir, MODEL_TRAINER_TRAINED_MODEL_NAME)


