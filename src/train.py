from sklearn.ensemble import RandomForestClassifier

import joblib

from config import MODEL_PATH


def train_model(X_train, y_train):

    print("\nTraining Model...\n")

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    joblib.dump(model, MODEL_PATH)

    print("Model Saved")

    return model
