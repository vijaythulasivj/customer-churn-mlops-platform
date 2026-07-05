import os
import shutil

from src.logger.logger import logger
from src.entity.config_entity import DataIngestionConfig


class DataIngestion:

    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def initiate_data_ingestion(self):

        logger.info("Starting Data Ingestion")

        os.makedirs(os.path.dirname(self.config.raw_data_path), exist_ok=True)

        source_file = "data/raw/customer_churn.csv"

        destination_file = self.config.raw_data_path

        if os.path.exists(source_file):

            shutil.copy(source_file, destination_file)

            logger.info("Dataset copied successfully")

        else:

            raise FileNotFoundError(
                f"{source_file} not found."
            )

        return destination_file
