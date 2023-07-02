# Airflow

Version and paramters definitions in [.env](.env)  

## Custom XCOM
To run Airflow with a Custom XCOM backend:
1. uncomment XCOM section in docker-compose.yml and 
1. run `minio`
1. set up the `bucket` and `access`/`secret` keys in minio ui and paste it to `./airflow/.env` file

## How to setup local development env for Airflow

Architecture:
- Dockerized Airflow from de-toolkit is perceived as dev, pre-prod, or prod stand.
- Local Airflow - same version of Airflow installed on developer's PC, into dev environment like IDE

### Steps:
1. Create venv 
    - `VSC > Ctrl+Shift+P > Python: Create Environment`
    - or `python -m venv .venv`
1. Activate venv `./.venv/bin/activate`
1. Install Airflow same version from [.env](.env) by instruction from [official website](https://airflow.apache.org/docs/apache-airflow/stable/installation/installing-from-pypi.html)
1. Init local Airflow instance `airflow db init`    
1. Start local Airflow instance `airflow standalone`
1. Optionally you can modify the local Airflow config in `~/airflow/airflow.cfg` . For example set DAGs folder:
    - `dags_folder = ~/ldev/de-toolkit/airflow/dags`
    - or change default webserver port `web_server_port = 8080`
1. Restart Airflow (Ctrl+C and run again)
1. Create Connections and Variables in your local Airflow instance by UI [http://localhost:8080](http://localhost:8080)

Now to run your code locally choose `./venv/bin/python` from `venv` as Python Interpreter. `VSC > Ctrl+Shift+P > Python: Select Interpreter`.

Open your DAG in IDE, run and debug it with breakpoints and other staff.