
# Apache_Airflow_Tutorial
&emsp;This repository provides an easy guide on Apache Airflow, explaining how to create, run, and manage data pipelines. It includes steps for installing Airflow using Docker, making the setup easier. The guide also covers basic concepts like DAGs (Directed Acyclic Graphs), which show workflows, and operators that define tasks in those workflows.

### Table of Contents
 - Basic concepts of Airflow
 - Code Example for Using a DAG
 - Install Apache Airflow using Docker
 - Accessing the Environment
 - Disclaimer

### Basic concepts of Airflow
<img src="https://fueled.com/the-cache/posts/backend/devops/mlops-with-airflow2/dag-task-operator.png" alt="diagram" width="600" />
picture from https://fueled.com/the-cache/posts/backend/devops/mlops-with-airflow2/dag-task-operator.png

#### 1. Directed Acyclic Graph (DAG):
&emsp;A DAG is a collection of all the tasks you want to run, organized in a way that reflects their relationships and dependencies. The DAG is "directed" because the tasks must be run in a specific order, and it's "acyclic" because it doesn't contain any cycles, meaning a task can’t depend on itself either directly or indirectly. In Airflow, DAGs define how tasks are scheduled and triggered, but the DAG itself does not perform any actions.<br>
Key Point: A DAG defines the structure and flow of tasks but doesn't execute them directly.
#### 2. Task:
&emsp;A task is a single unit of work within a DAG. Each task represents a specific operation, such as pulling data from a database, processing data, or sending an email notification. In Airflow, a task is defined by an Operator and can be subject to scheduling, retry logic, and other runtime behaviors.<br>
Key Point: Tasks are the individual pieces of work within a DAG.
#### 3. Operator:
&emsp;Operators are templates that define what actions a task should perform. Airflow provides different operators for different types of tasks, such as: <br>
BashOperator: Executes a bash command.<br>
PythonOperator: Executes a Python function.<br>
EmailOperator: Sends an email.<br>
Key Point: An operator defines what action a task will perform.
#### 4. Executor:
&emsp;The executor is responsible for running the tasks defined by the DAG. It defines how and where tasks are executed. There are different types of executors in Airflow, such as:<br>
SequentialExecutor: Runs tasks one by one.<br>
LocalExecutor: Runs tasks in parallel on the local machine.<br>
Key Point: The executor determines how tasks are distributed and executed across resources.

### Code Example for Using a DAG
&emsp; The code example will be in the dags directory, containing files such as:<br>
- bash_DAG.py : code example for bash operator.<br>
- python_DAG.py : code example for python operator.<br>
- CatchUp_explain_DAG.py : How to use and set the Catchup parameter.<br>
- taskflow_API_DAG.py : How to create a DAG using the TaskFlow API.<br>
- cron_in_DAG.py : How to schedule your DAG using a Cron expression.<br>

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
### Accessing the Environment
After starting Airflow, you can interact with it in three ways:

1. Via a browser using the web interface.
2. By using the REST API.
3. By running CLI commands.

#### 1. Accessing the Web Interface

The webserver is available at [http://localhost:8080](http://localhost:8080). The default login credentials are:
- **Username:** airflow
- **Password:** airflow

#### 2. Sending Requests to the REST API

The webserver is also available at [http://localhost:8080](http://localhost:8080). The default login credentials are:
- **Username:** airflow
- **Password:** airflow

**Example command to send a request to the REST API:**
```bash
ENDPOINT_URL="http://localhost:8080/"
curl -X GET  \
    --user "airflow:airflow" \
    "${ENDPOINT_URL}/api/v1/pools"
```
### Disclaimer
 - https://www.youtube.com/watch?v=K9AnJ9_ZAXE&list=PLwFJcsJ61oujAqYpMp1kdUBcPG0sE0QMT
 - https://airflow.apache.org/docs/apache-airflow/stable/index.html



