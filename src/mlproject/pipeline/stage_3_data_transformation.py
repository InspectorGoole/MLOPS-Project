from mlproject.config.configurations import ConfigurationManager
from mlproject.components.data_transformation import DataTransformation
from mlproject import logger 
from pathlib import Path 

STAGE_NAME = "Data Transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass 

    def main(self):
        try:
            with open(Path('artifacts/data_validation/status.txt'), 'r') as f: # checks if the data validation status in the status file is True
                status = f.read().split(' ')[-1]

            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.preprocessing()
            else: # if not true then the pipeline won't run bcuz the data validation is not True
                raise Exception('Your data schema is not valid')
            
        except Exception as e:
            print(e) 

if __name__ == "__main__":
    try:
        logger.info(f'>>>>stage {STAGE_NAME} started <<<<<')
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f'>>>>> stage {STAGE_NAME} Training completed <<<<<')
    except Exception as e:
        logger.exception(e)
        raise e 
