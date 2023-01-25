import os, sys

from src.constant.s3_bucket import *
from src.logger import logging as lg
from src.exception import SketchtocodeException

from src.cloud_storage.aws_syncer import S3Sync
from src.entity.training_entity.config_entity import DataIngestionConfig, AwsS3Config
from src.entity.training_entity.artifact_entity import DataIngestionArtifact


class DataIngestion:

    def __init__(self, data_ingestion_config: DataIngestionConfig) -> None:
        self.s3_syncer = S3Sync()
        self.data_ingestion_config = data_ingestion_config
        self.aws_s3_config = AwsS3Config()

    def get_object_detection_data(self):

        """
            Method Name :   get_object_detection_data
            Description :   This method downloads the object detection data from s3 bucket
            Output      :   NA
            On Failure  :   Write an exception log and then raise an exception

            Version     :   1.2
            Revisions   :   moved setup to cloud
        """

        try:
            self.s3_syncer.sync_folder_from_s3(
                aws_folder_path=self.aws_s3_config.obj_det_dataset_path,
                folder=self.data_ingestion_config.object_detection_data_store_dir
            )

            lg.info("obj detection data download complete")

        except Exception as e:
            raise SketchtocodeException(e, sys)

    def get_text_detection_data(self):
        """
            Method Name :   get_text_detection_data
            Description :   This method downloads the text detection data from s3 bucket
            Output      :   NA
            On Failure  :   Write an exception log and then raise an exception

            Version     :   1.2
            Revisions   :   moved setup to cloud
        """

        try:
            self.s3_syncer.sync_folder_from_s3(
                aws_folder_path=self.aws_s3_config.text_det_dataset_path,
                folder=self.data_ingestion_config.text_detection_data_store_dir
            )

            lg.info("text detection data download complete")
        except Exception as e:
            raise SketchtocodeException(e, sys)

    def get_object_detection_coco_annot_instances(self):

        """
            Method Name :   get_object_detection_coco_annot_instances
            Description :   This method downloads the object detection coco instances from s3 bucket
            Output      :   NA
            On Failure  :   Write an exception log and then raise an exception

            Version     :   1.2
            Revisions   :   moved setup to cloud
        """

        try:
            self.s3_syncer.sync_folder_from_s3(
                aws_folder_path=self.aws_s3_config.obj_det_coco_annot_path,
                folder=self.data_ingestion_config.object_detection_coco_annot_data_store_dir
            )

            lg.info("obj detection annot data download complete")
        except Exception as e:
            raise SketchtocodeException(e, sys)

    def get_text_detection_coco_annot_instances(self):

        """
            Method Name :   get_text_detection_coco_annot_instances
            Description :   This method downloads the text detection coco instances from s3 bucket
            Output      :   NA
            On Failure  :   Write an exception log and then raise an exception

            Version     :   1.2
            Revisions   :   moved setup to cloud
        """

        try:
            self.s3_syncer.sync_folder_from_s3(
                aws_folder_path=self.aws_s3_config.text_det_coco_annot_path,
                folder=self.data_ingestion_config.text_detection_coco_annot_data_store_dir
            )

            lg.info("text detection annot data download complete")
        except Exception as e:
            raise SketchtocodeException(e, sys)

    def initiate_data_ingestion(self) -> DataIngestionArtifact:

        """
            Method Name :   initiate_data_ingestion
            Description :   This method initiates the data ingestion component of the training pipeline
            Output      :   NA
            On Failure  :   Write an exception log and then raise an exception

            Version     :   1.2
            Revisions   :   moved setup to cloud
        """
        try:
            lg.info("Entered the data ingestion component of the training pipeline.")
            self.get_object_detection_data()
            self.get_text_detection_data()
            self.get_object_detection_coco_annot_instances()
            self.get_text_detection_coco_annot_instances()

            lg.info("Exited the data ingestion component.")

            data_ingestion_artifact = DataIngestionArtifact(
                obj_detection_training_data_folder_path=self.data_ingestion_config.obj_detection_train_data_dir,
                obj_detection_testing_data_folder_path=self.data_ingestion_config.obj_detection_test_data_dir,
                obj_detection_coco_train_annot_path=self.data_ingestion_config.obj_detection_train_coco_annot_path,
                obj_detection_coco_test_annot_path=self.data_ingestion_config.obj_detection_test_coco_annot_path,

                text_detection_training_data_folder_path=self.data_ingestion_config.text_detection_train_data_dir,
                text_detection_testing_data_folder_path=self.data_ingestion_config.text_detection_test_data_dir,
                text_detection_coco_train_annot_path=self.data_ingestion_config.text_detection_train_coco_annot_path,
                text_detection_coco_test_annot_path=self.data_ingestion_config.text_detection_test_coco_annot_path

            )

            return data_ingestion_artifact
        except Exception as e:
            raise SketchtocodeException(e, sys)
