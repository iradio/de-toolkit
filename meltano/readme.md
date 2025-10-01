# Meltano

## Getting started
https://docs.meltano.com/getting-started

## My steps
python3 -m venv venv  
source ./venv/bin/activate  
pip install pipx
pipx ensurepath
pipx install meltano

meltano --version

meltano init tutorial

meltano add extractor tap-gitlab
meltano add loader target-postgres
meltano add transformer dbt
meltano add orchestrator airflow

If you encounter this error:
```
Installing orchestrator 'airflow'...
Orchestrator 'airflow' could not be installed: failed to install plugin 'airflow'.
ERROR: 404 Client Error: Not Found for url: https://raw.githubusercontent.com/apache/airflow/constraints-2.1.2/constraints-3.10.txt

Failed to install plugin(s)
```
Use this workaround by changing the Airflow version in `meltano.yaml`:
```
BEFORE:
orchestrators:
  - name: airflow
    variant: apache
    pip_url: apache-airflow==2.1.2 --constraint https://raw.githubusercontent.com/apache/airflow/constraints-2.1.2/constraints-${MELTANO__PYTHON_VERSION}.txt 
AFTER:
orchestrators:
  - name: airflow
    variant: apache
    pip_url: apache-airflow==2.3.3 --constraint https://raw.githubusercontent.com/apache/airflow/constraints-2.3.3/constraints-${MELTANO__PYTHON_VERSION}.txt 
```
