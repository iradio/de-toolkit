# de-toolkit is toolkit and sandbox for Data Engineers
`de-toolkit` is a collection of open-source software designed for self-study as a data engineer. The kit is built on top of `docker` and `docker-compose`. 
The repository contains docker-compose files that deploy products on the de-toolkit-network shared virtual network, as well as the necessary configuration files, initialization, and examples to demonstrate how the tools work.

`de-toolkit` includes tools and systems from categories such as:
- ETL / ELT
- Databases
- DWH management
- BI
- Data Analysis

**The project is created and delivered for educational purposes.**
**Don't use `de-toolkit` in production!**

## Data Engineer Toolkit
| Product | Local ports | Local address | Credentials | Internal hostname |
| --- | --- | --- | --- | --- | 
| **Processing** |
| [Airflow](./airflow) | 8000 | [http://localhost:8000](http://localhost:8000) | l: `de_user`, p: `de_pass` | airflow* |
| [Airbyte](./airbyte) | 8100, 8101, 8102 | [http://localhost:8100](http://localhost:8100)|  l: `de_user`, p: `de_pass`  | airbyte* |
| [Dagster](./dagster) | 8200 | [http://localhost:8200](http://localhost:8200)| *no auth* | dagster |
| [Prefect2](./prefect2) | 4200 | [http://localhost:4200](http://localhost:4200) | *no auth* [Docs](https://docs.prefect.io/)  | prefect* |
| [Spark](./spark) | 8400 | [http://localhost:8400](http://localhost:8400) | *no auth* use check [spark/readme.md](./spark/readme.md) | spark, `spark://spark:7077` |
| [Cronicle](./cronicle) | 8500 |  [http://localhost:8500](http://localhost:8500) | l: `admin`, p: `admin`  | cronicle |
| [Meltano](./meltano/) | 5000 | [http://localhost:5000](http://localhost:5000) | *no auth* | meltano* |
| **Storage** |
| [PostgresSQL](./postgresql) | 5432 |  `postgresql://de_user:de_pass@localhost:5432/de` | db: `de`, l: `de_user`, p: `de_pass` | postgresql | 
| [ClickHouse](./clickhouse/) | 8123, 9000 | [http://localhost:8123/play](http://localhost:8123/play), `clickhouse+http://de_user:de_pass@localhost:8123/de`, `clickhouse+native://de_user:de_pass@localhost:9000/de` | db: `de`, l: `de_user`, p: `de_pass` | clickhouse |
| [MongoDB](./mongodb/) | 27017 | `mongodb://de_user:de_pass@localhost:27017/de` | db: `de`, l: `de_user`, p: `de_pass` | mongodb |
| [Minio](./minio/) | 9001,9002 |  [http://localhost:9001](http://localhost:9001) | l: `de_user`, p: `de_password` | minio |
| **DWH building** |
| [dbt](./dbt/) | 7000 | [http://localhost:7000](http://localhost:7000) | *no auth* | dbt* |
| **Visualization** |
| [Metabase](./metabase/) | 3000 | [http://localhost:3000](http://localhost:3000) | *set user on first start* | metabase |  
| [Superset](./superset/) | 3001 | [http://localhost:3001](http://localhost:3001) | l: `de_user`, p: `de_pass` | superset* |
| **Analytics** |
| [Jupyter](./jupyter/) | 4000 |  [http://localhost:4000](http://localhost:4000) | p: `de_pass` [change password instruction](./jupyter/notebooks/change_jypyter_pass.ipynb) | jupyter |
| **Metadata** |
| [Open Metadata](./openmetadata/) | 8585,8586, 8587, 9200, 9300|  [http://localhost:8585](http://localhost:8585) | l: `admin`, p: `admin` | omd-* |
| [Open Data Discovery](./opendatadiscovery/) | 9400 |  [http://localhost:9400](http://localhost:9400) | no auth | odd-* |

## Quick start
``` bash
git clone https://github.com/iradio/de-toolkit.git
cd de-toolkit
```
Select the product and run it via `docker-compose`.  Some products should be launched with the build flag, so it's better to use it by default. For example, start `Postgres`.
```bash
cd postgresql
docker-compose up -d --build
```

All products starts with access to the same shared network `de-toolkit-network`, and are accessible by hostname matching the server name.
For example: when connecting Postgresql to the Metabase product, you have to use hostname: `postgresql` as the DBMS address.

## Requirements
- `docker`
- `docker-compose`

Windows - [Docker Desktop with WSL 2 backend](https://docs.docker.com/desktop/windows/wsl/)

Mac - [Docker Desktop on Mac](https://docs.docker.com/desktop/install/mac-install/)

Linux - [Docker Desktop on Linux](https://docs.docker.com/desktop/install/linux-install/)

Sufficient amount of available docker RAM. More than 8GB.

How to check available docker memory:
``` bash
docker run --rm "debian:bullseye-slim" bash -c 'numfmt --to iec $(echo $(($(getconf _PHYS_PAGES) * $(getconf PAGE_SIZE))))' 
```
P.S.: tested on `Windows 10 Home 64 + Docker Desktop on WSL2` . Hardware: `Intel i7-10710U 64GB RAM SSD`


## Defaults 
Environment variables have definitions in the `.env` file. Each directory has a `.env` file inside (which can be hidden by default in your OS).  
Default credentials:  
username: `de_user`  
password: `de_pass`  


## Author
- Tim Alein - [iradio](https://github.com/iradio)