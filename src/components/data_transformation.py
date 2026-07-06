import os
import joblib
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split

from src.logger.logger import logger


class DataTransformation:

    def __init__(self, config):
        self.config = config

    def initiate_data_transformation(self, validated_data_path):

        logger.info("Starting Data Transformation")

        df = pd.read_csv(validated_data_path)

        print("\n========== DATA TRANSFORMATION ==========")

        # -----------------------------
        # Remove Customer ID
        # -----------------------------
        if "customerID" in df.columns:
            df.drop(columns=["customerID"], inplace=True)

        # -----------------------------
        # Convert TotalCharges
        # -----------------------------
        df["TotalCharges"] = pd.to_numeric(
            df["TotalCharges"],
            errors="coerce"
        )

        # -----------------------------
        # Fill Missing Values
        # -----------------------------
        df.fillna(0, inplace=True)
        # Encode target column
        df["Churn"] = df["Churn"].map({
            "No": 0,
            "Yes": 1
        })

        # -----------------------------
        # Split Features and Target
        # -----------------------------
        X = df.drop(columns=["Churn"])
        y = df["Churn"]

        # -----------------------------
        # Identify categorical columns
        # -----------------------------
        categorical_columns = X.select_dtypes(
            include=["object"]
        ).columns.tolist()

        # -----------------------------
        # Categorical Pipeline
        # -----------------------------
        categorical_pipeline = Pipeline(
            steps=[
                (
                    "imputer",
                    SimpleImputer(strategy="most_frequent")
                ),
                (
                    "encoder",
                    OneHotEncoder(handle_unknown="ignore")
                )
            ]
        )

        # -----------------------------
        # Column Transformer
        # -----------------------------
        preprocessor = ColumnTransformer(
            transformers=[
                (
                    "categorical",
                    categorical_pipeline,
                    categorical_columns
                )
            ],
            remainder="passthrough"
        )

        # -----------------------------
        # Transform Features
        # -----------------------------
        X = preprocessor.fit_transform(X)

        print("Features transformed successfully.")

        # -----------------------------
        # Save Preprocessor
        # -----------------------------
        os.makedirs(
            os.path.dirname(self.config.preprocessor_path),
            exist_ok=True
        )

        joblib.dump(
            preprocessor,
            self.config.preprocessor_path
        )

        print(
            f"Preprocessor saved to : {self.config.preprocessor_path}"
        )

        # -----------------------------
        # Train Test Split
        # -----------------------------
        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=self.config.test_size,
            random_state=42
        )

        # -----------------------------
        # Save Transformed Dataset
        # -----------------------------
        os.makedirs(
            os.path.dirname(self.config.train_data_path),
            exist_ok=True
        )

        joblib.dump(
            (X_train, y_train),
            self.config.train_data_path
        )

        joblib.dump(
            (X_test, y_test),
            self.config.test_data_path
        )

        logger.info("Data Transformation Completed")

        print(f"Train Shape : {X_train.shape}")
        print(f"Test Shape  : {X_test.shape}")

        return (
            self.config.train_data_path,
            self.config.test_data_path
        )
