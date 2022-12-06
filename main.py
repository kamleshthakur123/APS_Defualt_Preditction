from Sensor.logger import logging
from Sensor.exception import SensorException
from Sensor.utils import get_collection_as_dataframe
from Sensor.Entity import config_entity
import sys,os



if __name__=="__main__":

     try:
          training_pipeline_config=config_entity.TrainingPipelineConfig()
          data_ingestion_config=config_entity.DataIngestionConfig(training_pipeline_config)
          print(data_ingestion_config.to_dict())
     except Exception as e:
          print(e)

