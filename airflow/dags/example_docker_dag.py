from airflow.decorators import dag, task
from airflow.providers.docker.operators.docker import DockerOperator

from datetime import datetime

@dag(start_date=datetime(2022,1,1), schedule="@weekly", catchup=False)
def docker_example_dag():

    @task()
    def dummy_task():
        pass

    docker_task = DockerOperator(
        task_id='docker_task',
        image='python:3.10-slim-buster',
        command='echo "Execution date is {{ ds }}")',
        docker_url='unix://var/run/docker.sock',
        network_mode='bridge',
        auto_remove=True,
        container_name='airflow-task-{{ ds }}',
        environment={
            'SOME_ENV': 'value'
        },
        private_environment={
            'SECRET_ENV': 'value'
        }
    )

    dummy_task() >> docker_task

dag = docker_example_dag()