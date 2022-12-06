import pandas as pd 
from Sensor.Config import mongo_client
from Sensor.logger import logging
from Sensor.exception import SensorException
import os,sys

def get_collection_as_dataframe(database_name:str,collection_name:str) ->pd.DataFrame:
    """
    Description:This function return collection as dataframe 
    ================================================================================
    Params:
    database_name:database_name
    collection_name:collection_name
    """
    try:
        logging.info("Reading data from database: {database_name} and collection {collection_name}")

        df=pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        logging.info(f"found columns: {df.columns}")
        if "_id" in df.columns:
            logging.info(f"droping column :_id")
            df=df.drop("_id",axis=1)
        logging.info(f"row and cols in df :{df.shape}")
        return df
        
    except Exception as e:
        raise SensorException(e, sys)
    
