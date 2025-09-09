from mlproject import logger
from mlproject.pipeline.stage_1_data_ingestion import DataIngestionTrainingPipeline
from mlproject.pipeline.stage_2_data_validation import DataValidationTrainingPipeline
from mlproject.pipeline.stage_3_data_transformation import DataTransformationTrainingPipeline
from mlproject.pipeline.stage_4_model_training import ModelTrainerTrainingPipeline

STAGE_NAME = 'Data Ingestion'

try:
    logger.info(f">>>>> stage {STAGE_NAME} <<<<< started")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main() # if u call the main method of the class it will start the entire pipeline
    logger.info(f'>>>> stage {STAGE_NAME} completed <<<<\n\nx=======x')
except Exception as e:
    logger.exception(e)
    raise e 


STAGE_NAME = "Data Validation stage"

try:
    logger.info(f'>>>> stage {STAGE_NAME} started <<<<')
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f'>>>> stage {STAGE_NAME} completed <<<<<\n\nx========x')
except Exception as e:
        logger.exception(e)
        raise e 


STAGE_NAME = "Data Transformation stage"

try:
    logger.info(f'>>>>stage {STAGE_NAME} started <<<<<')
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f'>>>>> stage {STAGE_NAME} Training completed <<<<<')
except Exception as e:
    logger.exception(e)
    raise e 


STAGE_NAME = "Model Training Stage"

try:
    logger.info(f'>>>> stage {STAGE_NAME} started <<<<')
    train_model = ModelTrainerTrainingPipeline()
    train_model.main()
    logger.info(f'>>>>> stage {STAGE_NAME} completed <<<<')
except Exception as e:
    logger.exception(e)
    raise e