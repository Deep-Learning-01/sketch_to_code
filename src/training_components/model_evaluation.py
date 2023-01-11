import os,sys
from src.logger import logging as lg
from src.exception import SketchtocodeException
from src.entity.training_entity.artifact_entity import ModelEvaluationArtifact, ModelTrainerArtifact, DataIngestionArtifact

from src.entity.training_entity.config_entity import ModelEvaluationConfig, AwsS3Config
from src.cloud_storage.aws_syncer import S3Sync
from src.utils import is_model_present_in_s3
from src.utils.common import setup_config


from detectron2.engine import default_setup
from detectron2.engine import default_argument_parser
from detectron2.config import get_cfg
from detectron2.engine.defaults import DefaultPredictor
from detectron2.data.datasets import register_coco_instances
from detectron2.evaluation import COCOEvaluator, inference_on_dataset
from detectron2.data import build_detection_test_loader


class ModelEvaluation:

    def __init__(self,
                data_ingestion_artifact: DataIngestionArtifact,
                model_trainer_artifact: ModelTrainerArtifact,
                model_evaluation_config: ModelEvaluationConfig ):


        self.model_evaluation_config = model_evaluation_config
        self.model_trainer_artifact = model_trainer_artifact
        self.data_ingestion_artifact = data_ingestion_artifact
        self.aws_s3_config = AwsS3Config()
        self.s3_sync = S3Sync()

    def get_best_models_from_s3(self):
        """
            Method Name :   get_best_model_from_s3
            Description :   This method downloads the best model from the s3.
                            

            Output      :   best model object
            On Failure  :   Write an exception log and then raise an exception

            Version     :   1.2
            Revisions   :   moved setup to cloud
        """
        try:
            obj_det_s3_model_dir_path = self.model_evaluation_config.obj_det_aws_s3_model_dir_path
            text_det_s3_model_dir_path = self.model_evaluation_config.text_det_aws_s3_model_dir_path

            #local artifacts dir

            obj_det_best_model_dir = self.model_evaluation_config.obj_det_best_model_dir
            text_det_best_model_dir = self.model_evaluation_config.text_det_best_model_dir

            #object detection model download 

            
            self.s3_sync.sync_folder_from_s3(aws_folder_path= obj_det_s3_model_dir_path,
            folder= obj_det_best_model_dir )
            lg.info("obj det model download complete")

            #text detection model download
            self.s3_sync.sync_folder_from_s3(aws_folder_path= text_det_s3_model_dir_path,
            folder= text_det_best_model_dir )
            lg.info("text det model download complete")

            lg.info("models downloaded.")

             
        except Exception as e:
            raise SketchtocodeException(e,sys)

    



    def evaluate_model(self,
                        weights_path:str,
                        trained_model_config_file_path: str, 
                        test_coco_ins_name:str,
                        output_dir:str,


                        ):
                        
        """
            Method Name :   evaluate_model
            Description :   This method evaluates a model.

            Output      :   model evaluation orderdict.
            On Failure  :   Write an exception log and then raise an exception

            Version     :   1.2
            Revisions   :   moved setup to cloud
        """
        try:
            

            config = setup_config(trained_model_config_file_path=trained_model_config_file_path,
                                weights_path= weights_path)

            predictor = DefaultPredictor(config)

            evaluator = COCOEvaluator(test_coco_ins_name, config, False, output_dir=output_dir)
            val_loader = build_detection_test_loader(config, test_coco_ins_name)

            result = inference_on_dataset(predictor.model, val_loader, evaluator)

            return result

            


        except Exception as e:
            raise SketchtocodeException(e,sys)


    
    def evaluate_obj_det_model(self):
        """
            Method Name :   evaluate_best_model
            Description :   This method evaluates the object detection model and 
                            compares with the best model.

            Output      :   is_model_accepted: bool
            On Failure  :   Write an exception log and then raise an exception

            Version     :   1.2
            Revisions   :   moved setup to cloud
        """
        try:
            register_coco_instances(name= self.model_evaluation_config.obj_detection_test_coco_ins_name,
                        metadata={},    
                        json_file= self.data_ingestion_artifact.obj_detection_coco_test_annot_path,
                        image_root= self.data_ingestion_artifact.obj_detection_testing_data_folder_path )

            #evaluate trained model from artifacts
            trained_model_weights = self.model_trainer_artifact.obj_detection_trained_model_file_path
            trained_model_config_file_path = self.model_trainer_artifact.obj_detection_trained_model_config_file_path
            
            trained_model_evaluation_result =  self.evaluate_model(weights_path= trained_model_weights,
                                trained_model_config_file_path= trained_model_config_file_path,
                                test_coco_ins_name= self.model_evaluation_config.obj_detection_test_coco_ins_name,
                                output_dir= self.model_evaluation_config.obj_detection_model_eval_output_dir)


            trained_model_ap = trained_model_evaluation_result['bbox']['AP']

            
            #evaluate best model
            s3_model_path = self.aws_s3_config.obj_det_model_path
        
            if is_model_present_in_s3(s3_model_path):

         

                best_model_weights = self.model_evaluation_config.obj_det_best_model_path
                best_model_config_file_path = self.model_evaluation_config.obj_det_best_model_config_file_path
                best_model_evaluation_result = self.evaluate_model(
                    weights_path= best_model_weights,
                    trained_model_config_file_path= best_model_config_file_path,
                    test_coco_ins_name= self.model_evaluation_config.obj_detection_test_coco_ins_name,
                    output_dir= self.model_evaluation_config.obj_detection_model_eval_output_dir
                )

                #ap: Average Precision
                best_model_ap = best_model_evaluation_result['bbox']['AP']

            else:
                best_model_ap = 0


            lg.info("object detection is evaluated. Best model Ap score is: %s" % best_model_ap)

            is_obj_det_trained_model_accepted = True if trained_model_ap > best_model_ap else False

            return is_obj_det_trained_model_accepted




        except Exception as e:
            raise SketchtocodeException(e,sys)




    def evaluate_text_det_model(self):
        """
            Method Name :   evaluate_text_det_model
            Description :   This method evaluates the text detection model and 
                            compares with the best model.

            Output      :   is_model_accepted: bool
            On Failure  :   Write an exception log and then raise an exception

            Version     :   1.2
            Revisions   :   moved setup to cloud
        """
        try:
            register_coco_instances(name= self.model_evaluation_config.text_detection_test_coco_ins_name,
                        metadata={},    
                        json_file= self.data_ingestion_artifact.text_detection_coco_test_annot_path,
                        image_root= self.data_ingestion_artifact.text_detection_testing_data_folder_path )

            #evaluate trained model from artifacts
            trained_model_weights = self.model_trainer_artifact.text_detection_trained_model_file_path
            trained_model_config_file_path = self.model_trainer_artifact.text_detection_trained_model_config_file_path
            
            trained_model_evaluation_result =  self.evaluate_model(weights_path= trained_model_weights,
                                trained_model_config_file_path= trained_model_config_file_path,
                                test_coco_ins_name= self.model_evaluation_config.text_detection_test_coco_ins_name,
                                output_dir= self.model_evaluation_config.text_detection_model_eval_output_dir)


            trained_model_ap = trained_model_evaluation_result['bbox']['AP']

            
            #evaluate best model
            s3_model_path = self.aws_s3_config.text_det_model_path
        
            if is_model_present_in_s3(s3_model_path):

         

                best_model_weights = self.model_evaluation_config.text_det_best_model_path
                best_model_config_file_path = self.model_evaluation_config.text_det_best_model_config_file_path
                best_model_evaluation_result = self.evaluate_model(
                    weights_path= best_model_weights,
                    trained_model_config_file_path= best_model_config_file_path,
                    test_coco_ins_name= self.model_evaluation_config.text_detection_test_coco_ins_name,
                    output_dir= self.model_evaluation_config.text_detection_model_eval_output_dir
                )

                #ap: Average Precision
                best_model_ap = best_model_evaluation_result['bbox']['AP']

            else:
                best_model_ap = 0

            is_text_det_trained_model_accepted = True if trained_model_ap > best_model_ap else False

            lg.info("Text detection is evaluated. Best model Ap score is: %s" % best_model_ap)


            return is_text_det_trained_model_accepted




        except Exception as e:
            raise SketchtocodeException(e,sys)

    def initiate_model_evaluation(self):
        """
            Method Name :   initiate_evaluation
            Description :   This method initiates the model evaluation component of the training pipeline. 

            Output      :   model evaluation artifact
            On Failure  :   Write an exception log and then raise an exception

            Version     :   1.2
            Revisions   :   moved setup to cloud
        """
        try:

            lg.info("Model evaluation is initiated.")

            self.get_best_models_from_s3()
            is_obj_det_model_accepted = self.evaluate_obj_det_model()
            is_text_det_model_accepted = self.evaluate_text_det_model()
            
            model_eval_artifact = ModelEvaluationArtifact(
                is_obj_det_model_accepted= is_obj_det_model_accepted,
                is_text_det_model_accepted= is_text_det_model_accepted
            )

            lg.info("Model evaluation is completed.")
            return model_eval_artifact

        except Exception as e:
            raise SketchtocodeException(e,sys)
