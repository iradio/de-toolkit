# Airflow

Version and parameter definitions are stored in [.env](.env).  

## Custom XCOM
To run Airflow with a Custom XCOM backend:
1. Uncomment the XCOM section in `docker-compose.yml`.
2. Run `minio`.
3. Set up the `bucket` and `access`/`secret` keys in the MinIO UI and paste them into the `./airflow/.env` file.

## How to set up a local development environment for Airflow

Architecture:
- Dockerized Airflow from de-toolkit represents a dev, pre-prod, or prod environment.
- Local Airflow uses the same Airflow version installed on the developer's machine and integrates with IDE tooling.

### Steps:
1. Create a virtual environment 
    - `VSC > Ctrl+Shift+P > Python: Create Environment`
    - or `python -m venv .venv`
1. Activate the virtual environment: `./.venv/bin/activate`
1. Install the Airflow version listed in [.env](.env) by following the [official instructions](https://airflow.apache.org/docs/apache-airflow/stable/installation/installing-from-pypi.html)
1. Initialize the local Airflow instance: `airflow db init`    
1. Start the local Airflow instance: `airflow standalone`
1. Optionally modify the local Airflow config in `~/airflow/airflow.cfg`. For example, set the DAGs folder:
    - `dags_folder = ~/ldev/de-toolkit/airflow/dags`
    - or change default webserver port `web_server_port = 8080`
1. Restart Airflow (Ctrl+C and run again)
1. Create Connections and Variables in your local Airflow instance via the UI: [http://localhost:8080](http://localhost:8080)

To run your code locally, select `./.venv/bin/python` from the virtual environment as the Python interpreter (`VSC > Ctrl+Shift+P > Python: Select Interpreter`).

Open your DAG in the IDE, then run and debug it with breakpoints and other tooling.
