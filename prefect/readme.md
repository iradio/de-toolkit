# PREFECT

Docs https://docs.prefect.io/orchestration/Server/deploy-local.html

Prefect Server can be deployed on a single node using docker-compose.

The easiest way accomplish this is to use the built-in command in the Prefect CLI. Note that this requires both docker-compose >= 1.18.0 and docker to be installed.

By default, Prefect is configured to use Prefect Cloud as the backend. To use Prefect Server as the backend, run the following Prefect CLI command to configure Prefect for local orchestration:
``` bash
$ prefect backend server
```     
Now you can start the server using the command:
``` bash
$ prefect server start
```
``` bash
prefect server start --postgres-url postgres://<username>:<password>@hostname:<port>/<dbname>
```

