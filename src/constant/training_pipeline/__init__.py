# pipeline name and root directory constant
import os
from src.constant.s3_bucket import TRAINING_BUCKET_NAME
from from_root import from_root

PIPELINE_NAME: str = "src"
ARTIFACT_DIR: str = "artifact"
TRAINING_ARTIFACT_DIR = "training_artifacts"

LOG_DIR = "logs"
LOG_FILE = "sktc.log"

# common file name
ROOT_DIR = from_root()
MODEL_CONFIG_FILE_PATH = os.path.join(ROOT_DIR,"config", "model_config.yaml")


"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_INGESTED_DIR: str = "ingested"

DATA_INGESTION_OBJ_DET_DIR: str = "object_detection"
DATA_INGESTION_TEXT_DET_DIR: str = "text_detection"

DATA_INGESTION_DATA_STORE_DIR: str = "dataset"
DATA_INGESTION_COCO_ANNOT_STORE_DIR: str = "annotations"

DATA_INGESTION_TRAIN_DIR: str = "train"
DATA_INGESTION_TEST_DIR: str = "test"

DATA_INGESTION_TRAIN_COCO_ANNOT_FILE_NAME: str = "train_annotations.coco.json"
DATA_INGESTION_TEST_COCO_ANNOT_FILE_NAME: str = "test_annotations.coco.json"





"""
MODEL TRAINER related constant start with MODEL_TRAINER var name
"""

MODEL_TRAINER_ARTIFACT_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_NAME: str = "model_final.pth"
MODEL_TRAINER_OBJ_DET_ARTIFACT_DIR_NAME: str = "object_detection"
MODEL_TRAINER_TEXT_DET_ARTIFACT_DIR_NAME: str = "text_detection"
MODEL_TRAINER_TRAINED_MODEL_OUTPUT_DIR: str ="saved_model"
MODEL_TRAINER_OBJ_DET_TRAIN_COCO_INS_NAME: str = "training_sketches"
MODEL_TRAINER_OBJ_DET_TEST_COCO_INS_NAME: str = "testing_sketches"
MODEL_TRAINER_TEXT_DET_TRAIN_COCO_INS_DIR: str = "training_texts"
MODEL_TRAINER_TEXT_DET_TEST_COCO_INS_DIR: str = "testing_texts"

MODEL_TRAINER_OBJ_DET_MODEL_YAML_FILE_DIR_NAME: str = "COCO-Detection"
MODEL_TRAINER_OBJ_DET_MODEL_YAML_CONFIG_FILE_NAME: str ="faster_rcnn_R_50_FPN_3x.yaml"

MODEL_TRAINER_TEXT_DET_MODEL_YAML_FILE_DIR_NAME: str =  "config"
MODEL_TRAINER_TEXT_DET_MODEL_YAML_CONFIG_FILE_NAME: str = "sign_faster_rcnn_R_101_FPN_3x.yaml"

# """
# MODEL Evauation related constant start with MODEL_EVALUATION var name
# """

# MODEL_EVALUATION_DIR_NAME:str = 'model_evaluation'
# MODEL_EVALUATION_BEST_MODEL_DIR:str =  "best_model"
# MODEL_EVALUATION_BEST_MODEL_NAME:str = MODEL_TRAINER_TRAINED_MODEL_NAME

# MODEL_PUSHER_BUCKET_NAME = TRAINING_BUCKET_NAME

