import sys
from typing import Tuple
import numpy as np

from src.exception import MyException
from src.logger import logging

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score,precision_score,recall_score,accuracy_score

from src.entity.config_entity import ModelTrainerConfig
from src.entity.artifact_entity import DataTransformationArtifact,ModelTrainerArtifact,ClassificationMetricArtifact
from src.utils.main_utils import load_numpy_array,load_object,save_object
from src.entity.estimator import MyModel

class ModelTrainer:
    def __init__(self,data_transformation_artifact:DataTransformationArtifact,model_trainer_config:ModelTrainerConfig):
        self.data_transformation_artifact = data_transformation_artifact
        self.model_trainer_config = model_trainer_config
        
    def get_model_object_and_report(self,train:np.array,test:np.array)->Tuple[object,object]:
        
        try:
            logging.info("Training RandomForestClassifier with specified parameters")
            x_train,y_train=train[:,:-1],train[:,-1]
            x_test,y_test=test[:,:-1],test[:,-1]
            logging.info("Splitted training and testing input data")    
            
            model=RandomForestClassifier(n_estimators=self.model_trainer_config._n_estimators,
                                         min_samples_split=self.model_trainer_config._min_samples_split,
                                         min_samples_leaf=self.model_trainer_config._min_samples_leaf,  
                                         max_depth=self.model_trainer_config._max_depth,
                                         criterion=self.model_trainer_config._criterion,    
                                         random_state=self.model_trainer_config._random_state
                                         )
            
            logging.info("Fitting the model")
            model.fit(x_train,y_train)      
            logging
            logging.info("Predicting the test data")
            y_pred=model.predict(x_test)        
            accuracy=accuracy_score(y_test,y_pred)
            precision=precision_score(y_test,y_pred)
            recall=recall_score(y_test,y_pred)
            f1=f1_score(y_test,y_pred)
            
            
            logging.info(f"Model training completed with accuracy: {accuracy}, precision: {precision}, recall: {recall}, f1_score: {f1}")
            
            metric_artifact=ClassificationMetricArtifact(f1_score=f1,
                                                         precision_score=precision,recall_score=recall)
            return model,metric_artifact
        except Exception as e:
            raise MyException (sys,e) from e    
        
    def initiate_model_trainer(self)->ModelTrainerArtifact:
        logging.info("Entered the initiate_model_trainer method of ModelTrainer class")
        try:
            print("........................................................")
            print("strating model training component")
            
            train_arr=load_numpy_array(file_path=self.data_transformation_artifact.transformed_train_file_path)
            test_arr=load_numpy_array(file_path=self.data_transformation_artifact.transformed_test_file_path)
            logging.info("Loaded training and testing array data")
            
            trained_model,metric_artifact=self.get_model_object_and_report(train=train_arr,test=test_arr)
            logging.info("Got trained model and metric artifact from get_model_object_and_report method")   
            
            preprocessing_obj=load_object(file_path=self.data_transformation_artifact.preprocessed_object_file_path)
            logging.info("Loaded preprocessing object")
            
            if accuracy_score(train_arr[:, -1],trained_model.predict(train_arr[:,:-1])) < self.model_trainer_config.expected_accuracy:
                raise Exception(f"Trained model accuracy is less than the expected accuracy {self.model_trainer_config.expected_accuracy}")
            
            logging.info("Saving the trained model object")
            my_model=MyModel(preprocessing_object=preprocessing_obj,trained_model_object=trained_model) 
            save_object(self.model_trainer_config.trained_model_file_path,my_model
                        )
            logging.info("Saved the trained model object successfully") 
            
            model_trainer_artifact=ModelTrainerArtifact(
                trained_model_file_path=self.model_trainer_config.trained_model_file_path,metric_artifact=metric_artifact)  
            
            logging.info("Exited the initiate_model_trainer method of ModelTrainer class")
            return model_trainer_artifact       
        except Exception as e:
            raise MyException (sys,e) from e
        