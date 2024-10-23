
# Apache_Airflow_Tutorial

&emsp;This repository offers an easy-to-follow guide on Apache Airflow, explaining the basics of creating, running, and managing data pipelines.

### Basic components of Airflow
<img src="https://fueled.com/the-cache/posts/backend/devops/mlops-with-airflow2/dag-task-operator.png" alt="diagram" width="600" />
picture from https://fueled.com/the-cache/posts/backend/devops/mlops-with-airflow2/dag-task-operator.png


#### 1. Directed Acyclic Graph (DAG):
A DAG is a collection of all the tasks you want to run, organized in a way that reflects their relationships and dependencies. The DAG is "directed" because the tasks must be run in a specific order, and it's "acyclic" because it doesn't contain any cycles, meaning a task can’t depend on itself either directly or indirectly. In Airflow, DAGs define how tasks are scheduled and triggered, but the DAG itself does not perform any actions.<br>
Key Point: A DAG defines the structure and flow of tasks but doesn't execute them directly.
#### 2. Task:
A task is a single unit of work within a DAG. Each task represents a specific operation, such as pulling data from a database, processing data, or sending an email notification. In Airflow, a task is defined by an Operator and can be subject to scheduling, retry logic, and other runtime behaviors.<br>
Key Point: Tasks are the individual pieces of work within a DAG.
#### 3. Operator:
Operators are templates that define what actions a task should perform. Airflow provides different operators for different types of tasks, such as: <br>
BashOperator: Executes a bash command.<br>
PythonOperator: Executes a Python function.<br>
EmailOperator: Sends an email.<br>
Key Point: An operator defines what action a task will perform.
#### 4. Executor:
The executor is responsible for running the tasks defined by the DAG. It defines how and where tasks are executed. There are different types of executors in Airflow, such as:<br>
SequentialExecutor: Runs tasks one by one.<br>
LocalExecutor: Runs tasks in parallel on the local machine.<br>
Key Point: The executor determines how tasks are distributed and executed across resources.

### Install Apache Airflow using Docker

1. Check that your Docker has more than 4 GB of RAM.
```bash
  docker run --rm "debian:bookworm-slim" bash -c "numfmt --to iec $(echo $(($(getconf _PHYS_PAGES) * $(getconf PAGE_SIZE))))"
```
2. Download the docker-compose.yaml file for Apache Airflow.
```bash
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.10.2/docker-compose.yaml'
```
&emsp;&emsp;&emsp;or
```bash
Invoke-WebRequest -Uri 'https://airflow.apache.org/docs/apache-airflow/2.10.2/docker-compose.yaml' -OutFile 'docker-compose.yaml'
```
&emsp;&emsp;&emsp;or 

just copy text from https://airflow.apache.org/docs/apache-airflow/2.10.2/docker-compose.yaml

3. Run mkdir to create directories: dags, logs, plugins, and config.
```bash
mkdir dags, logs, plugins, config
```
4. Create a .env file to declare AIRFLOW_UID.
```bash
$AIRFLOW_UID = [System.Security.Principal.WindowsIdentity]::GetCurrent().User.Value
echo "AIRFLOW_UID=$AIRFLOW_UID" > .env
```
&emsp;&emsp;&emsp;or
```bash
echo "AIRFLOW_UID=50000" > .env
```
&emsp;&emsp;&emsp;or 

create .env file and paste AIRFLOW_UID=50000

5. Run
```bash
docker-compose up airflow-init
```
6. Run 
```bash
docker-compose up
```
7. Install Apache Airflow python library using
```bash
pip install apache-airflow
```


