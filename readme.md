# Набор инстурментов и sandbox начинающего Data Engineer
`de-toolkit` - набор open source программного обеспечения, предназначенный для самостоятельного обучения профессии инженера данных. Набор построен на основе `docker` и представляет собой варианты компоновки преднастроенного ПО (далее - **сборки**) в виде `docker-compose.yaml` файлов и преднастроенных каталогов вида `product-name` с файлами конфигурации, пресетами и каталогами для монтирования `volumes`.

Сборки включают продукты как минимум из трех категорий: **ETL DB BI** (но это не точно).

Проект создается и поставляется в образовательных целях.

Не используейте `de-toolkit` в production!

## Требования к окружению
Работает везде, где есть:
- `docker`
- `docker-compose`

Windows - [Docker Desktop with WSL 2 backend](https://docs.docker.com/desktop/windows/wsl/)

Mac - [Docker Desktop on Mac](https://docs.docker.com/desktop/install/mac-install/)

Linux - [Docker Desktop on Linux](https://docs.docker.com/desktop/install/linux-install/)

Достаточный объем доступной docker оперативной памяти. Нужно более 4GB. 

Можно проверить командой:

``` bash
docker run --rm "debian:bullseye-slim" bash -c 'numfmt --to iec $(echo $(($(getconf _PHYS_PAGES) * $(getconf PAGE_SIZE))))' 
```
P.S.: на текущий момент автор собирает и тестирует сборки на `Windows 10 Home 64 + Docker Desktop on WSL2` . Hardware: `Intel i7-10710U 16GB RAM SSD`

## Быстрый старт
``` bash
git clone https://github.com/iradio/de-toolkit.git
cd de-toolkit
```
Далее выбираем нужную сборку и запускаем указанной командой:

### Build: Postgres + Metabase
``` bash
docker-compose up docker-compose_pg_metabase.yml
```
Postgres: `postgresql://pg_user:pg_pass@localhost:5432/de`   
Metabase: http://localhost:3000 *set user on first start*  

### Build: Postgres + ClickHouse + Metabase
``` bash
docker-compose up docker-compose_pg_ch_metabase.yml
```
Postgres: `postgresql://pg_user:pg_pass@localhost:5432/de`  
ClickHouse: `clickhouse+http://pg_user:pg_pass@localhost:8123/de` , `clickhouse+native://pg_user:pg_pass@localhost:9000/de`  
Metabase: http://localhost:3000 *set user on first start*  

### Build: Cronicle + Postgres + Metabase
``` bash
docker-compose up docker-compose_cronicle_pg_metabase.yml
```
Cronicle: http://localhost:8080 `admin`/`admin`  
Postgres: `postgresql://pg_user:pg_pass@localhost:5432/de`  
Metabase: http://localhost:3000 *will create user on first start*  

### Build: Airflow + Postgres + Metabase
``` bash
docker-compose up docker-compose_airflow_pg_metabase.yml
```
Airflow: http://localhost:8080 `de_user`/`de_pass`  
Postgres: `postgresql://pg_user:pg_pass@localhost:5432/de`  
Metabase: http://localhost:3000 *will create user on first start*

### Build: Airbyte + Postgres + Metabase
``` bash
docker-compose up docker-compose_airbyte_pg_metabase.yml
```
Airbyte: http://localhost:8080 *set user on first start*  
Postgres: `postgresql://pg_user:pg_pass@localhost:5432/de`  
Metabase: http://localhost:3000 *set user on first start*

### Build: Spark + Jupyter + Postgres + Metabase
``` bash
docker compose -f "docker-compose_spark_jupyter_pg_metabase.yml" up -d --scale spark-worker=3
```
Where `--scale spark-worker=3` means the number of spark workers in your cluster.  

Spark: http://localhost:8080 *no auth* use check [spark/readme.md](./spark/readme.md)
Jupyter http://localhost:8888 `de_pass` [change password instruction](./jupyter/notebooks/change_jypyter_pass.ipynb)  
Postgres: `postgresql://pg_user:pg_pass@localhost:5432/de`  
Metabase: http://localhost:3000 *set user on first start*

### Build: Prefect + Postgres + Metabase
``` bash
docker-compose up docker-compose_prefect_pg_metabase.yaml
```
Prefect: http://localhost:8080 *no auth* use `prefect` console. [Docs](https://docs.prefect.io/)  
Postgres: `postgresql://pg_user:pg_pass@localhost:5432/de`  
Metabase: http://localhost:4000 *set user on first start*

## Defaults 
Переменные заданые в [.env файле](.env) (файл может быть скрыт в вашей системе).  
По умолчанию везде, где можно используются:  
username: `de_user`  
password: `de_pass`  

## ПО, включенное в сборку
### СУБД
```
├── PostgreSQL
├── MongoDB *todo*
├── ClickHouse
```
### ETL | ELT
```
├── Комплексные ETL | ELT
│   ├── Airflow
│   ├── Cronicle
│   ├── Spark
│   ├── Prefect
│   ├── Luigi *todo*
│   ├── StreamSets *todo*
├── E(xtract) *todo*
│   ├── Airbyte
├── L(oad) *todo*
│   ├── Airbyte
├── T(ransform) *todo*
│   ├── dbt
```
### BI
```
├── Metabase
├── Superset *todo*
```
### IDE 
├── Jupyter

## Авторы
- Тимур Алейников - [iradio](https://github.com/iradio)