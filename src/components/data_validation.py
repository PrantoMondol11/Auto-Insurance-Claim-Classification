import json
import sys
import os

import pandas as pd
from pandas import DataFrame

from src.exception import MyException
from src.logger import logging

from src.utils.main_utils import read_yaml_file,write_yaml_file
from src.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact
from src.entity.config_entity import DataValidationConfig
from src.constants import SCHEMA_FILE_PATH


class DataValidation:
    def __init__(self,data_ingestion_artifact:DataIngestionArtifact,data_validation_config:DataValidationConfig):
        try:
            self.data_ingestion_artifact=data_ingestion_artifact
            self.data_validation_config=data_validation_config
            self._schema_config=read_yaml_file(file_path=SCHEMA_FILE_PATH)
        except Exception as e:
            raise MyException (sys,e ) 
    def validate_number_of_columns(self,dataframe:DataFrame) -> bool:
        try:
            status=len(dataframe.columns)==len(self._schema_config["columns"])
            logging.info(f"Is required colmn present: [{status}]")
            return status
        
        except Exception as e:
            raise MyException (sys,e)
        
    def is_colmn_exist(self,df:DataFrame)-> bool:
        try:
            dataframe_colums=df.columns
            missing_numerical_columns=[]
            missing_catagorical_columns=[]
            for column in self._schema_config["numerical_columns"]:
                if column not in dataframe_colums:
                    missing_numerical_columns.append(column)
            if len(missing_numerical_columns)>0:
                logging.info(f"Missing numerical column : {missing_numerical_columns}")
                    
            for column in self._schema_config["catagorical_columns"]:
                if column not in dataframe_colums:
                    missing_catagorical_columns.append(column)
            if len(missing_catagorical_columns)>0:
                logging.info(f"Missing catagorical column : {missing_numerical_columns}")
            return False if len(missing_catagorical_columns)>0 or len(missing_numerical_columns)>0 else True
        except Exception as e:
            raise MyException (sys,e) from e
        
    @staticmethod
    def read_data(file_path) -> DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise MyException (e,sys)
                