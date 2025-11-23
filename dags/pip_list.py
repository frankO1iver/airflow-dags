from airflow import DAG
# В Airflow 3 BashOperator переехал в стандартный провайдер
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 11, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'pip_list',
    default_args=default_args,
    description='return pip list',
    schedule=timedelta(days=1),  # было schedule_interval
    catchup=False,
) as dag:

    show_packages = BashOperator(
        task_id="show_packages",
        bash_command="pip3 list"
    )
