from mlproject.config.configurations import ConfigurationManager
from mlproject.components.model_trainer import ModelTrainer
from mlproject import logger 


STAGE_NAME = 'Model trainer stage'

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config() # getting our model trainer config
        model_trainer_config = ModelTrainer(config=model_trainer_config) # applying the model_trainer_config to our modeltrainer
        model_trainer_config.train() # trainging the model


if __name__ == '__main__':
    try:
        logger.info(f'>>>> stage {STAGE_NAME} started <<<<')
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f'>>>>> stage {STAGE_NAME} completed <<<<')
    except Exception as e:
        logger.exception(e)
        raise e