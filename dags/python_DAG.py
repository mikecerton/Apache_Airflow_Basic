from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

my_default_args = {
    'owner': 'itsMe!!',
    'retries': 2,
    'retry_delay': timedelta(minutes=2)
}

def say_hi():
    print("hello its me !!!")

def greet_with_parameter(name, age):
    print(f"hello my name is {name}, {age}")

def greet_wth_xcom(ti):
    first_name = ti.xcom_pull(task_ids='task_A', key='first_name')
    last_name = ti.xcom_pull(task_ids='task_A', key='last_name')
    age = ti.xcom_pull(task_ids='task_B', key='age')
    print(f"Hello World! My name is {first_name} {last_name}, "
          f"and I am {age} years old!")

def get_name(ti):
    ti.xcom_push(key='first_name', value='Timmy')
    ti.xcom_push(key='last_name', value='Wellson')

def get_age(ti):
    ti.xcom_push(key='age', value=21)  

with DAG(
    dag_id='normal_python_DAG',
    description='normal_python_DAG',
    default_args=my_default_args,
    start_date=datetime(2024, 10, 16),  
    schedule='@daily',         
    catchup=False,
) as dag:

    task1 = PythonOperator(
        task_id = "task_1",
        python_callable=say_hi
    )

    task1

with DAG(
    dag_id='parameter_python_DAG',
    description='python task with parameter',
    default_args=my_default_args,
    start_date=datetime(2024, 10, 16),  
    schedule='@daily',         
    catchup=False,
) as dag:
    
    task1 = PythonOperator(
        task_id = "task_1",
        python_callable=greet_with_parameter,
        op_kwargs={'name' : 'timmy', 'age' : 5}
    )

    task1

with DAG(
    dag_id='xcom_python_DAG',
    description='xcom_python_DAG',
    default_args=my_default_args,
    start_date=datetime(2024, 10, 16),  
    schedule='@daily',         
    catchup=False,
) as dag:
    
    task_A = PythonOperator(
        task_id = "task_A",
        python_callable=get_name
    )
    task_B = PythonOperator(
        task_id = "task_B",
        python_callable=get_age
    )
    task_C = PythonOperator(
        task_id = "task_c",
        python_callable=greet_wth_xcom
    )

    [task_A, task_B]>>task_C