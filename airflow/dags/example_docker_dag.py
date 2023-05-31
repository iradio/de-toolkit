from airflow.decorators import dag, task
from airflow.providers.docker.operators.docker import DockerOperator

from datetime import datetime

@dag(start_date=datetime(2022,1,1), schedule="@weekly", catchup=False)
def docker_example_dag():
    @task()
    
    def t1():
        pass

    t2 = DockerOperator(
        task_id='t2',
        image='python:3.10-slim-buster',
        command='echo "Execution date is {{ ds }}")',
        docker_url='unix://var/run/docker.sock',
        network_mode='bridge'
    )

    t1() >> t2

dag = docker_example_dag()