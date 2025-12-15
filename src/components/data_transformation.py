import sys
import numpy as np
import pandas as pd
from imblearn.combine import SMOTEENN
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler,StandardScaler
from sklearn.compose import ColumnTransformer

from src.exception import MyException
from src.logger import logging
from src.constants import TARGET_COLUMN,SCHEMA_FILE_PATH,CURRENT_YEAR
from src.entity.config_entity import DataTransformationConfig
from src.entity.artifact_entity import DataTransformationArtifact,DataIngestionArtifact,DataValidationArtifact
from src.utils.main_utils import save_object,save_numpy_array_data,read_yaml_file


class DataTransformation:
    def __init__(self,
                 data_ingestion_artifact:DataIngestionArtifact,
                 data_validation_artifact:DataValidationArtifact,
                 data_transformation_config:DataTransformationConfig):
        try:
            self.data_ingestion_artifact=data_ingestion_artifact
            self.data_validation_artifact=data_validation_artifact
            self.data_transformation_config=data_transformation_config
            self._schema_config=read_yaml_file(file_path=SCHEMA_FILE_PATH)
        except Exception as e:
            raise MyException (sys,e) from e
        
    @staticmethod
    def read_data(file_path)->pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise MyException (sys,e) from e
        
    def get_data_transformer_object(self)->Pipeline:
        
        logging.info("Entered the get_data_transformer_object method of DataTransformation class")  
        
        try:
           numerical_transformer=StandardScaler()
           min_max_scaler=MinMaxScaler()
           logging.info("Transformer Initialized: StandardScaler and MinMaxScaler")
           
           num_features=self._schema_config["num_features"]
           nm_columns=self._schema_config["mm_columns"]
           logging.info("columns loaded from schema file")

           preprocessor=ColumnTransformer(transformers=[
               ("StandardScaler",numerical_transformer,num_features),
               ("MinMaxScaler",min_max_scaler,nm_columns)
           ],
                                          remainder="passthrough")
           final_pipeline=Pipeline(steps=[("preprocessor",preprocessor)])
           logging.info("Pipeline created successfully")    
           logging.info("Exited the get_data_transformer_object method of DataTransformation class")
           return final_pipeline
        except Exception as e:
            raise MyException (sys,e) from e
    
    def _map_gender(self,df:pd.DataFrame):
        try:
            logging.info("Mapping gender column to binary values")
            df["Gender"] = df["Gender"].map({"Male": 0, "Female": 1}).astype(int)
            logging.info("Gender column mapped successfully")
            return df
        except Exception as e:
            raise MyException (sys,e) from e
        
    def _rename_columns(self,df:pd.DataFrame):
        try:
            logging.info("Renaming columns to remove spaces and special characters")
            df= df.rename(columns={"Vehicle_Age_<1 Year":"Vehicle_Age_lt_1_Year",
                                   "Vehicle_Age_>2 Years":"Vehicle_Age_gt_2_Years"})
            
            for col in ["Vehicle_Age_lt_1_Year","Vehicle_Age_gt_2_Years","Vehicle_Damage_Yes"]:
                if col in df.columns:
                    df[col]=df[col].astype('int')

            logging.info("Columns renamed successfully")
            return df
        except Exception as e:
            raise MyException (sys,e) from e
        
    def _drop_id_column(self,df:pd.DataFrame):
        try:
            logging.info("Dropping ID column from the dataframe")
            drop_col=self._schema_config["drop_columns"]
            if drop_col in df.columns:
                df=df.drop(columns=[drop_col],axis=1)
            logging.info("ID column dropped successfully")
            return df
        except Exception as e:
            raise MyException (sys,e) from e
    def _create_dummy_columns(self,df:pd.DataFrame):
        logging.info("Creating dummy variables for categorical columns")
        try:
            df=pd.get_dummies(df,drop_first=True)
            logging.info("Dummy variables created successfully")
            return df
        except Exception as e:
            raise MyException (sys,e) from e
    
    def initiate_data_transformation(self)->DataTransformationArtifact:
        try:
            logging.info("Entered the initiate_data_transformation method of DataTransformation class")     
            
            if not self.data_validation_artifact.validation_status:
                raise Exception (f"Data Validation failed. Error message :{self.data_validation_artifact.message}")     
            
            train_df=DataTransformation.read_data(self.data_ingestion_artifact.trained_file_path)
            test_df=DataTransformation.read_data(self.data_ingestion_artifact.test_file_path)
            logging.info("Read train and test data as dataframe")
            
            logging.info("Applying preprocessing on training and testing dataframe")
            input_feature_train_df=train_df.drop(columns=[TARGET_COLUMN],axis=1)
            target_feature_train_df=train_df[TARGET_COLUMN] 
            input_feature_test_df=test_df.drop(columns=[TARGET_COLUMN],axis=1)
            target_feature_test_df=test_df[TARGET_COLUMN] 
            
              
            input_feature_train_df=self._map_gender(input_feature_train_df)
            input_feature_test_df=self._map_gender  (input_feature_test_df)
            input_feature_train_df=self._drop_id_column(input_feature_train_df)
            input_feature_test_df=self._drop_id_column(input_feature_test_df)
            input_feature_train_df=self._rename_columns(input_feature_train_df)         
            input_feature_test_df=self._rename_columns(input_feature_test_df)
            input_feature_train_df=self._create_dummy_columns(input_feature_train_df)         
            input_feature_test_df=self._create_dummy_columns(input_feature_test_df) 
            
            logging.info("Custom transformations applied successfully")
            
            logging.info("Starting data transformation")
            preprocessor=self.get_data_transformer_object()
            logging.info("Got preprocessor object")
            
            logging.info("Applying preprocessor object on training and testing dataframe")
            input_feature_train_arr=preprocessor.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessor.transform(input_feature_test_df)
            logging.info("Applied preprocessor object on training and testing dataframe successfully")
            
            logging.info("Applying SMOTEENN on training and testing data")
            smt=SMOTEENN(sampling_strategy="minority")
            input_feature_train_final,target_feature_train_final=smt.fit_resample(input_feature_train_arr,target_feature_train_df)
            input_feature_test_final,target_feature_test_final=smt.fit_resample(input_feature_test_arr,target_feature_test_df)
            logging.info("Applied SMOTEENN on training and testing data successfully")  
            
            train_arr=np.c_[input_feature_train_final,np.array(target_feature_train_final)]
            test_arr=np.c_[input_feature_test_final,np.array(target_feature_test_final)] 
            logging.info("Concatenated input features and target feature array to form train and test array")   
            
            save_object(self.data_transformation_config.transformed_object_file_path,preprocessor)
            save_numpy_array_data(self.data_transformation_config.transformed_train_file_path,array=train_arr  )
            save_numpy_array_data(self.data_transformation_config.transformed_test_file_path,array=test_arr  )
            logging.info("Saved transformed object and numpy array data successfully")  
            
            logging.info("Data tranformation completed")
            return DataTransformationArtifact(
                transformed_train_file_path=self.data_transformation_config.transformed_train_file_path,
                transformed_test_file_path=self.data_transformation_config.transformed_test_file_path,
                preprocessed_object_file_path=self.data_transformation_config.transformed_object_file_path)
            
        except Exception as e:
            raise MyException (sys,e) from e