import os
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from src.logger.logger import logger


class DataTransformation:

    def __init__(self, config):
        self.config = config

    def initiate_data_transformation(self, validated_data_path):

        logger.info("Starting Data Transformation")

        df = pd.read_csv(validated_data_path)

        print("\n========== DATA TRANSFORMATION ==========")

        # Remove Customer ID
        if "customerID" in df.columns:
            df.drop(columns=["customerID"], inplace=True)

        # Convert TotalCharges to numeric
        df["TotalCharges"] = pd.to_numeric(
            df["TotalCharges"],
            errors="coerce"
        )

        # Fill missing values
        df.fillna(0, inplace=True)

        # Encode categorical columns
        encoder = LabelEncoder()

        for column in df.columns:

            if df[column].dtype == "object":

                df[column] = encoder.fit_transform(df[column])

        print("Categorical columns encoded successfully.")

        # Split train and test
        train_df, test_df = train_test_split(
            df,
            test_size=0.2,
            random_state=42,
            shuffle=True
        )

        os.makedirs(
            os.path.dirname(self.config.train_data_path),
            exist_ok=True
        )

        train_df.to_csv(
            self.config.train_data_path,
            index=False
        )

        test_df.to_csv(
            self.config.test_data_path,
            index=False
        )

        logger.info("Data Transformation Completed")

        print(f"Train Shape : {train_df.shape}")
        print(f"Test Shape  : {test_df.shape}")

        return (
            self.config.train_data_path,
            self.config.test_data_path
        )
