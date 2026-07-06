import os
import joblib

from sklearn.ensemble import RandomForestClassifier

from src.logger.logger import logger


class ModelTrainer:

    def __init__(self, config):
        self.config = config

    def initiate_model_training(self, train_data_path):

        logger.info("Starting Model Training")

        print("\n========== MODEL TRAINING ==========")

        # ---------------------------------
        # Load transformed training data
        # ---------------------------------
        X_train, y_train = joblib.load(train_data_path)

        # ---------------------------------
        # Train Random Forest Model
        # ---------------------------------
        model = RandomForestClassifier(
            n_estimators=self.config.n_estimators,
            random_state=self.config.random_state
        )

        model.fit(X_train, y_train)

        print("RandomForest model trained successfully.")

        # ---------------------------------
        # Save trained model
        # ---------------------------------
        os.makedirs(
            os.path.dirname(self.config.model_path),
            exist_ok=True
        )

        joblib.dump(
            model,
            self.config.model_path
        )

        print(f"Model saved to : {self.config.model_path}")

        logger.info("Model Training Completed")

        return self.config.model_path
