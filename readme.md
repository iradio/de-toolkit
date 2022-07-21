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
### Сборка: Cronicle + Postgres + Metabase
``` bash
git clone https://github.com/iradio/de-toolkit.git
cd de-toolkit
docker-compose up docker-compose_cronicle_pg_metabase.yml
```
Cronicle: http://localhost:8080 admin/admin

Postgres: postgresql://pg_user:pg_pass@localhost:5432/de

Metabase: http://localhost:3000 *will create user on first start*

### Сборка: Airflow + Postgres + Metabase
``` bash
git clone https://github.com/iradio/de-toolkit.git
cd de-toolkit
docker-compose up docker-compose_airflow_pg_metabase.yml
```
Airflow: http://localhot:8080 de_user/de_pass

Postgres: postgresql://pg_user:pg_pass@localhost:5432/de 

Metabase: http://localhost:3000 *will create user on first start*

### Сборка: Airbyte + Postgres + Metabase
``` bash
git clone https://github.com/iradio/de-toolkit.git
cd de-toolkit
docker-compose up docker-compose_airbyte_pg_metabase.yml
```
Airbyte: http://localhot:8080 *set user on first start*

Postgres: postgresql://pg_user:pg_pass@localhost:5432/de 

Metabase: http://localhost:3000 *set user on first start*

## Defaults 

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
│   ├── Luigi *todo*
│   ├── StreamSets *todo*
├── E(xtract) *todo*
│   ├── Airbyte
├── L(oad) *todo*
│   ├── Airbyte
├── T(ransform) *todo*
│   ├── dbt *todo*
```
### BI
```
├── Metabase
├── Superset *todo*
```
## Авторы
- Тимур Алейников - [iradio](https://github.com/iradio)