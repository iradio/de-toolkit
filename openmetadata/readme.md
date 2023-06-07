# Open Metadata
Metadata management solution that includes data discovery, governance, data quality, observability, and people collaboration.

# How to use

1. Run OpenMetadata
```bash
docker-compose up -d
```

2. Run other services to ingest metadata from:
```bash
cd ../postgresql
docker-compose up -d
cd ../airflow
docker-compose up -d
cd ../metabase
docker-compose up -d
```

3. Set up connections to running services using Open Metadata UI.

[Databases](http://localhost:8585/settings/services/databases)
![postgresql](./img/postgresql.png)

[Dashboards](http://localhost:8585/settings/services/dashboards)
![metabase](./img/metabase.png)

[Pipelines](http://localhost:8585/settings/services/pipelines)
![airflow](./img/airflow.png)