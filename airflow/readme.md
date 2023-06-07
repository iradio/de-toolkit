# Airflow

Version and paramters definitions in [.env](.env)  

To run Airflow with a Custom XCOM backend:
1. uncomment XCOM section in docker-compose.yml and 
1. run `minio`
1. set up the `busket` and `access`/`secret` keys in minio ui and paste it to `./airflow/.env` file