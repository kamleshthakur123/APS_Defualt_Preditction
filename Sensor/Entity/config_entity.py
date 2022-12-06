import os,sys
from datetime import datetime
from Sensor.exception import SensorException
from Sensor.logger import logging
FILE_NAME='sensor.csv'
TRAIN_FILE_NAME='train.csv'
TEST_FILE_NAME='test.csv'
TEST_SIZE=.2


class TrainingPipelineConfig:
    
    def __init__(self):
        try:

            self.artifact_dir=os.path.join(os.getcwd(),"artifact",f"{datetime.now().strftime('%m%d%Y__%H%M%S')}")
        except Exception as e:
            raise SensorException(e, sys)



class DataIngestionConfig:

    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        try:

            self.database_name='aps'
            self.collection_name='sensor'
            self.data_ingestion_dir=os.path.join(TrainingPipelineConfig().artifact_dir,"dataIngestion")
            self.feature_store_file_path = os.path.join(self.data_ingestion_dir,"feature_store",FILE_NAME)
            self.train_file_path=os.path.join(self.data_ingestion_dir,'dataset',TRAIN_FILE_NAME)
            self.test_file_path=os.path.join(self.data_ingestion_dir,'dataset',TEST_FILE_NAME)
            self.test_size=TEST_SIZE
        except Exception as e:
            raise SensorException(e, sys)

    
    def to_dict(self,)->dict:
        try:
            return self.__dict__
        except Exception as e:
            raise SensorException(e,sys)
        


class DataValidationConfig:...
class DataTransformationConfig:...
class ModelTrainerConfig:...
class ModelEvaluationConfig:...
class ModelPusherConfig:...
