
# Apache_Airflow_Tutorial

This repository contains a comprehensive guide to get started with Apache Airflow. It includes step-by-step instructions, code examples.

### install Apache Airflow using docker

1. Check that your Docker has more than X GB of RAM.
```bash
  docker run --rm "debian:bookworm-slim" bash -c "numfmt --to iec $(echo $(($(getconf _PHYS_PAGES) * $(getconf PAGE_SIZE))))"
```
2. Download the docker-compose.yaml file for Apache Airflow.
```bash
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.10.2/docker-compose.yaml'
```
or
```bash
Invoke-WebRequest -Uri 'https://airflow.apache.org/docs/apache-airflow/2.10.2/docker-compose.yaml' -OutFile 'docker-compose.yaml'
```
or 

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
or
```bash
echo "AIRFLOW_UID=50000" > .env
```
or 

create .env and paste AIRFLOW_UID=50000

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


