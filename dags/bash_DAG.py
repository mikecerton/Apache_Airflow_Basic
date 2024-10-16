from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

my_default_args = {
    'owner': 'itsMe!!',
    'retries': 2,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='normal_bash_DAG',
    description='normal_bash_DAG',
    default_args=my_default_args,
    start_date=datetime(2024, 10, 16),  
    schedule_interval='@daily',         
    catchup=False,
) as dag:

    task_1 = BashOperator(
        task_id='task_1',
        bash_command='echo "task_1 at $(date +\'%T\')"'
    )
    task_2 = BashOperator(
        task_id='task_2',
        bash_command='echo "task_2 at $(date +\'%T\')"'
    )
    task_3 = BashOperator(
        task_id='task_3',
        bash_command='echo "task_3 at $(date +\'%T\')"'
    )
    task_4 = BashOperator(
        task_id='task_4',
        bash_command='echo "task_4 at $(date +\'%T\')"'
    )
    
    task_1>>[task_2, task_3]>>task_4
