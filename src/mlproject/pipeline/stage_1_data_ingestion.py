from mlproject.config.configurations import ConfigurationManager
from mlproject.components.data_ingestion import DataIngestion
from mlproject import logger 

STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass 

    def main(self):
        config = ConfigurationManager() # initializing the configuration manager
        data_ingestion_config = config.get_data_ingestion_config()  # from configuration manager i am calling the get_data_ingestion config
        data_ingestion = DataIngestion(config=data_ingestion_config) # return the top to the DataIngestion class
        data_ingestion.download_file() # then calling the download function to download the file
        data_ingestion.extract_zip_file() # then unzipping the file


if __name__ == '__main__':
    try:
        logger.info(f'>>>> stage {STAGE_NAME} started <<<<<<')
        obj = DataIngestionTrainingPipeline
        obj.main()
        logger.info(f">>>>> {STAGE_NAME} completed <<<<<<\n\nx=======x")
    except Exception as e:
        logger.exception(e)
        raise e