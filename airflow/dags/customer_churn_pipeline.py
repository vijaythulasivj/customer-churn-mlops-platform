from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

from src.pipeline.training_pipeline import TrainingPipeline


def run_pipeline():
    pipeline = TrainingPipeline()
    pipeline.start_pipeline()


with DAG(
    dag_id="customer_churn_training_pipeline",
    start_date=datetime(2026, 7, 1),
    schedule="@daily",
    catchup=False,
    tags=["mlops", "customer-churn"],
) as dag:

    training_pipeline = PythonOperator(
        task_id="training_pipeline",
        python_callable=run_pipeline,
    )
