# PREFECT

Docs: https://docs.prefect.io/orchestration/Server/deploy-local.html

Prefect Server can be deployed on a single node using docker-compose.

The easiest way to accomplish this is to use the built-in command in the Prefect CLI. Note that this requires docker-compose >= 1.18.0 and Docker to be installed.

By default, Prefect is configured to use Prefect Cloud as the backend. To switch to Prefect Server, run the following CLI command to configure Prefect for local orchestration:
```bash
prefect backend server
```
Now you can start the server using:
```bash
prefect server start
```
Or specify a custom Postgres connection:
```bash
prefect server start --postgres-url postgres://<username>:<password>@hostname:<port>/<dbname>
```

# Write the first DAG

Tutorial: https://docs.prefect.io/core/tutorial/01-etl-before-prefect.html
