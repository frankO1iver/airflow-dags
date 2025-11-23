from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta
import time

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 11, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def hello_world():
    print("Hello from Airflow in Kubernetes!")
    time.sleep(120)
    return "Success"

with DAG(
    'example_hello_world',
    default_args=default_args,
    description='Simple example DAG',
    schedule=timedelta(days=1),  # было schedule_interval
    catchup=False,
) as dag:

    for i in range(10):
        task = PythonOperator(
            task_id=f'hello_task_{i+1}',
            python_callable=hello_world,
        )
