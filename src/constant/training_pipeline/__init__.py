# pipeline name and root directory constant
import os
from src.constant.s3_bucket import TRAINING_BUCKET_NAME


PIPELINE_NAME: str = "src"
ARTIFACT_DIR: str = "artifact"
TRAINING_ARTIFACT_DIR = "training_artifacts"

LOG_DIR = "logs"
LOG_FILE = "sktc.log"

# common file name




"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_INGESTED_DIR: str = "ingested"

DATA_INGESTION_OBJ_DET_DIR: str = "object_detection"
DATA_INGESTION_TEXT_DET_DIR: str = "text_detection"

DATA_INGESTION_DATA_STORE_DIR: str = "dataset"
DATA_INGESTION_ANNOT_STORE_DIR: str = "annotations"

DATA_INGESTION_TRAIN_DIR: str = "train"
DATA_INGESTION_TEST_DIR: str = "test"


"""
Data Transformation ralated constant start with DATA_TRANSFORMATION VAR NAME
"""

DATA_TRANSFORMATION_TARGET_IMAGE_SIZE:tuple = (48,48)
DATA_TRANSFORMATION_BATCH_SIZE:int = 128


"""
MODEL TRAINER related constant start with MODEL_TRAINER var name
"""
MODEL_TRAINER_ARTIFACT_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR: str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME: str = "model.h5"
MODEL_TRAINER_NO_OF_EPOCH: float = 2
MODEL_TRAINER_TRAINED_MODEL_BASE_ACC_SCORE = 0.5

"""
MODEL Evauation related constant start with MODEL_EVALUATION var name
"""

MODEL_EVALUATION_DIR_NAME:str = 'model_evaluation'
MODEL_EVALUATION_BEST_MODEL_DIR:str =  "best_model"
MODEL_EVALUATION_BEST_MODEL_NAME:str = MODEL_TRAINER_TRAINED_MODEL_NAME

MODEL_PUSHER_BUCKET_NAME = TRAINING_BUCKET_NAME

