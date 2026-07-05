import joblib
import pandas as pd

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

from src.logger.logger import logger


class ModelEvaluation:

    def __init__(self):
        pass

    def initiate_model_evaluation(
        self,
        model_path,
        test_data_path
    ):

        logger.info("Starting Model Evaluation")

        model = joblib.load(model_path)

        test_df = pd.read_csv(test_data_path)

        X_test = test_df.drop(columns=["Churn"])

        y_test = test_df["Churn"]

        predictions = model.predict(X_test)

        accuracy = accuracy_score(
            y_test,
            predictions
        )

        precision = precision_score(
            y_test,
            predictions
        )

        recall = recall_score(
            y_test,
            predictions
        )

        f1 = f1_score(
            y_test,
            predictions
        )

        print("\n========== MODEL EVALUATION ==========")

        print(f"Accuracy  : {accuracy:.4f}")

        print(f"Precision : {precision:.4f}")

        print(f"Recall    : {recall:.4f}")

        print(f"F1 Score  : {f1:.4f}")

        logger.info("Model Evaluation Completed")
