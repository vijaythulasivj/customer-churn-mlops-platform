import joblib

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)

from src.logger.logger import logger


class ModelEvaluation:

    def __init__(self, config=None):
        self.config = config

    def initiate_model_evaluation(
        self,
        model_path,
        test_data_path
    ):

        logger.info("Starting Model Evaluation")

        print("\n========== MODEL EVALUATION ==========")

        # ---------------------------------
        # Load trained model
        # ---------------------------------
        model = joblib.load(model_path)

        # ---------------------------------
        # Load transformed test data
        # ---------------------------------
        X_test, y_test = joblib.load(test_data_path)

        # ---------------------------------
        # Make predictions
        # ---------------------------------
        y_pred = model.predict(X_test)

        # ---------------------------------
        # Calculate Metrics
        # ---------------------------------
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)

        print(f"Accuracy  : {accuracy:.4f}")
        print(f"Precision : {precision:.4f}")
        print(f"Recall    : {recall:.4f}")
        print(f"F1 Score  : {f1:.4f}")

        logger.info("Model Evaluation Completed")

        return {
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "f1_score": f1
        }
