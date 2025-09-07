import os 
import urllib.request as request  # to download data from url
import zipfile # to unzip the data
from mlproject import logger  # if u want to do some logging
from mlproject.utils.common import get_size  # to check size
from pathlib import Path
from mlproject.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config 

# this will create a directory called data ingestion and then it will download the data from given url and the save the log
    def download_file(self): 
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f'File already exists of size: {get_size(Path(self.config.local_data_file))}')
 
    def extract_zip_file(self): # this function will unzip the file and save it in the certain folder
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok= True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)  