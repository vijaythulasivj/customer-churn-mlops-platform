import os
import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier

from src.logger.logger import logger


class ModelTrainer:

    def __init__(self, config):
        self.config = config

    def initiate_model_training(self, train_data_path):

        logger.info("Starting Model Training")

        train_df = pd.read_csv(train_data_path)

        # Target column
        X_train = train_df.drop(columns=["Churn"])
        y_train = train_df["Churn"]

        # Train model
        model = RandomForestClassifier(
            n_estimators=100,
            random_state=42
        )

        model.fit(X_train, y_train)

        os.makedirs(
            os.path.dirname(self.config.model_path),
            exist_ok=True
        )

        joblib.dump(
            model,
            self.config.model_path
        )

        logger.info("Model saved successfully")

        print("\n========== MODEL TRAINING ==========")
        print("RandomForest model trained successfully.")
        print(f"Model saved to : {self.config.model_path}")

        return self.config.model_path
