from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

my_default_args = {
    'owner': 'itsMe!!',
    'retries': 2,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='CatchUp_explain_DAG',
    default_args=my_default_args,
    start_date=datetime(2024, 10, 16),
    schedule_interval='@daily',
    catchup=True                        # normally catchup default will be True anyway
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command='echo "print at $(date +\'%T\')"'
    )

    task1