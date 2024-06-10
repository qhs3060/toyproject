import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_error, accuracy_score, r2_score
from sklearn.datasets import load_iris
import logging

# Logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def train_and_predict(california_data, iris_data):
    try:
        # Convert California housing data to DataFrame
        california_dicts = [item.as_dict() for item in california_data]
        california_df = pd.DataFrame(california_dicts)
        california_df.columns = california_df.columns.str.lower()  # 컬럼 이름 소문자화
        X_california = california_df.drop(columns=['id', 'medhouseval'])
        y_california = california_df['medhouseval']

        # Train model on California housing data
        X_train, X_test, y_train, y_test = train_test_split(X_california, y_california, test_size=0.2, random_state=42)
        model = LinearRegression()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        california_rmse = root_mean_squared_error(y_test, y_pred)
        california_r2 = r2_score(y_test, y_pred)

        # Convert Iris data to DataFrame
        iris_dicts = [item.as_dict() for item in iris_data]
        iris_df = pd.DataFrame(iris_dicts)
        iris_df.columns = iris_df.columns.str.lower()  # 컬럼 이름 소문자화
        X_iris = iris_df.drop(columns=['id', 'target'])
        y_iris = iris_df['target']

        # For demonstration purposes, use preloaded iris dataset for training
        iris = load_iris()
        X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)
        model = LinearRegression()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        iris_rmse = root_mean_squared_error(y_test, y_pred)
        iris_r2 = r2_score(y_test, y_pred)

        # To calculate accuracy, we round the predictions and compare with the actual target
        y_pred_rounded = y_pred.round().astype(int)
        iris_accuracy = accuracy_score(y_test, y_pred_rounded)

        return {
            "california_rmse": california_rmse, 
            "california_r2": california_r2,
            "iris_rmse": iris_rmse, 
            "iris_r2": iris_r2,
            "iris_accuracy": iris_accuracy
        }
    except Exception as e:
        logger.error(f"Error during model training and prediction: {e}")
        raise
