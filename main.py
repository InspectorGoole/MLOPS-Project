from mlproject import logger
from mlproject.pipeline.stage_1_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = 'Data Ingestion'

try:
    logger.info(f">>>>> stage {STAGE_NAME} <<<<< started")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main() # if u call the main method of the class it will start the entire pipeline
    logger.info(f'>>>> stage {STAGE_NAME} completed <<<<\n\nx=======x')
except Exception as e:
    logger.exception(e)
    raise e 

