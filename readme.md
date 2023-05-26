# de-toolkit is toolkit and sandbox for Data Engineers
`de-toolkit` - набор open source программного обеспечения, предназначенный для самостоятельного обучения профессии инженера данных. Набор построен на основе `docker` и представляет собой репозиторий `docker-compose` инструкций по развертыванию продуктов в общей виртуальной сети `de-toolkit-network`, а также необходимых файлов конфигурации, инициализации и примеров для демонстрации работы инструментов.

В `de-toolkit` включаются инструменты и системы из таких категорий как:
- ETL / ELT
- Databases
- DWH management
- BI
- Data Analysis

**Проект создается и поставляется в образовательных целях.**  
**Не используейте `de-toolkit` в production!**

## Data Engineer Toolkit
| Product | Local ports | Local address | Credentials | Internal hostname |
| --- | --- | --- | --- | --- | 
| **Processing** |
| [Airflow](./airflow) | 8000 | [http://localhost:8000](http://localhost:8000) | l: `de_user`, p: `de_pass` | airflow* |
| [Airbyte](./airbyte) | 8100, 8101, 8102 | [http://localhost:8100](http://localhost:8100)|  l: `de_user`, p: `de_pass`  | airbyte* |
| [Dagster](./dagster) | 8200 | [http://localhost:8200](http://localhost:8200)| *no auth* | dagster |
| [Prefect](./prefect) | 8300 | TBD | *no auth* use `prefect` console. [Docs](https://docs.prefect.io/)  | prefect* |
| [Spark](./spark) | 8400 | [http://localhost:8400](http://localhost:8400) | *no auth* use check [spark/readme.md](./spark/readme.md) | spark, `spark://spark:7077` |
| [Cronicle](./cronicle) | 8500 |  [http://localhost:8500](http://localhost:8500) | l: `admin`, p: `admin`  | cronicle |
| [Meltano](./meltano/) | TBD | TBD | TBD | TBD|
| **Storage** |
| [PostgresSQL](./postgresql) | 5432 |  `postgresql://de_user:de_pass@localhost:5432/de` | db: `de`, l: `de_user`, p: `de_pass` | postgresql | 
| [ClickHouse](./clickhouse/) | 8123, 9000 | [http://localhost:8123/play](http://localhost:8123/play), `clickhouse+http://de_user:de_pass@localhost:8123/de`, `clickhouse+native://de_user:de_pass@localhost:9000/de` | db: `de`, l: `de_user`, p: `de_pass` | clickhouse |
| [MongoDB](./mongodb/) | 27017 | `mongodb://de_user:de_pass@localhost:27017/de` | db: `de`, l: `de_user`, p: `de_pass` | mongodb |
| **DWH building** |
| [dbt](./dbt/) | 9000 | [http://localhost:9000](http://localhost:9000) | *no auth* | dbt* |
| **Visualization** |
| [Metabase](./metabase/) | 3000 | [http://localhost:3000](http://localhost:3000) | *set user on first start* | metabase |  
| [Superset](./superset/) | 3001 | [http://localhost:3001](http://localhost:3001) | l: `de_user`, p: `de_pass` | superset* |
| **Analytics** |
| [Jupyter](./jupyter/) | 4000 |  [http://localhost:4000](http://localhost:4000) | p: `de_pass` [change password instruction](./jupyter/notebooks/change_jypyter_pass.ipynb) | jupyter |


## Quick start
``` bash
git clone https://github.com/iradio/de-toolkit.git
cd de-toolkit
```
Далее выбираем нужный продукт и запускаем его через `docker-compose`. Например, старт `Postgres`. Часть продуктов запускается с флагном build, поэтому лучше использовать его по умолчанию.
```bash
cd postgresql
docker-compose up -d --build
```

Все продукты запускаются с доступом к одной общей сети `de-toolkit-network` и доступны по hostname совпадающим с именем сервера.  
Например: при подключении Postgresql к продукту Metabase нужно использовать в качестве адрес СУБД hostname: `postgresql`.


## Requirements
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
P.S.: на текущий момент автор собирает и тестирует сборки на `Windows 10 Home 64 + Docker Desktop on WSL2` . Hardware: `Intel i7-10710U 64GB RAM SSD`



## Defaults 
Environment variables have definitions in the `.env` file. Each directory has a `.env` file inside (which can be hidden by default in your OS).  
Default credentials:  
username: `de_user`  
password: `de_pass`  


## Авторы
- Timur Aleinikov - [iradio](https://github.com/iradio)