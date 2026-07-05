import os
import pandas as pd

from src.logger.logger import logger


class DataValidation:

    def __init__(self, config):
        self.config = config

    def initiate_data_validation(self, raw_data_path):

        logger.info("Starting Data Validation")

        if not os.path.exists(raw_data_path):
            raise FileNotFoundError(f"{raw_data_path} not found")

        df = pd.read_csv(raw_data_path)

        print("\n========== DATA VALIDATION ==========")

        print(f"Rows    : {df.shape[0]}")
        print(f"Columns : {df.shape[1]}")

        if df.empty:
            raise Exception("Dataset is empty.")

        missing_values = df.isnull().sum()

        print("\nMissing Values")

        print(missing_values)

        duplicate_rows = df.duplicated().sum()

        print(f"\nDuplicate Rows : {duplicate_rows}")

        os.makedirs(
            os.path.dirname(
                self.config.validated_data_path
            ),
            exist_ok=True
        )

        df.to_csv(
            self.config.validated_data_path,
            index=False
        )

        logger.info("Validation Completed")

        print("\nValidated dataset saved successfully.")

        return self.config.validated_data_path
