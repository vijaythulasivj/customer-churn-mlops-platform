import os
import shutil

from src.logger.logger import logger


class DataIngestion:

    def __init__(self, config):
        self.config = config

    def initiate_data_ingestion(self):

        logger.info("Starting Data Ingestion")

        os.makedirs(
            os.path.dirname(self.config.raw_data_path),
            exist_ok=True
        )

        shutil.copy(
            self.config.source_data_path,
            self.config.raw_data_path
        )

        logger.info("Dataset copied successfully.")

        print("\n========== DATA INGESTION ==========")
        print("Dataset copied successfully.")
        print(f"Source      : {self.config.source_data_path}")
        print(f"Destination : {self.config.raw_data_path}")

        return self.config.raw_data_path
