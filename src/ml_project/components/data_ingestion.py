import os
import urllib.request as request
from ml_project import logger
from zipfile import ZipFile
from pathlib import Path
from ml_project.utils.common import get_size
from ml_project.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig) -> None:
        self.config = config

    # Download the data in the form of zip format from the given url.
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(
                f"{filename} download! wiht the following info: \n{headers}")
        else:
            logger.info(
                f"File already exists of size: {get_size(Path(self.config.local_data_file))}")

    # Extract the data from the zip file.
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip fkile in to data directory.
        Function returns None.
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with ZipFile(self.config.local_data_file, "r") as file:
            file.extractall(unzip_path)
