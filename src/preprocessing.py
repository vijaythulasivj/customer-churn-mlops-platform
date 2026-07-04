from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

from config import TARGET_COLUMN
from config import TEST_SIZE
from config import RANDOM_STATE


def preprocess(df):

    encoder = LabelEncoder()

    categorical_columns = df.select_dtypes(include="object").columns

    for column in categorical_columns:

        df[column] = encoder.fit_transform(df[column])

    X = df.drop(TARGET_COLUMN, axis=1)

    y = df[TARGET_COLUMN]

    return train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE
    )
