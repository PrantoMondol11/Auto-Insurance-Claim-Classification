# from src.logger import logging
# from src.exception import MyException
# import sys
# try:
#     a=1+"x"
# except Exception as e:
#     logging.info(e)
#     raise MyException(e,sys) from e

# logging.debug("This is a debug msg")
from src.pipeline.training_pipeline import TrainPipeline
pipline=TrainPipeline()
pipline.run_pipeline()
