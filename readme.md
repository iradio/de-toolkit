# Набор инстурментов и sendbox начинающего Data Engineer
`de-toolkit` - набор open source программного обеспечения, предназначенный для самостоятельного обучения профессии инженера данных. Набор построен на основе `docker` и представляет собой варианты компоновки преднастроенного ПО в виде `docker-compose.yaml` файлов.

Сборка создавалась и поставляется в образовательных целях.

Не используейте `de-toolkit` в production!

## Требования к окружению
Работает везде, где есть:
- `docker`
- `docker-compose`

Windows - [Docker Desktop with WSL 2 backend](https://docs.docker.com/desktop/windows/wsl/)

Mac - [Docker Desktop on Mac](https://docs.docker.com/desktop/install/mac-install/)

Linux - [Docker Desktop on Linux](https://docs.docker.com/desktop/install/linux-install/)

## Быстрый старт
``` bash
git clone https://github.com/iradio/de-toolkit.git
cd de-toolkit
docker-compose up
```


## Сборки инструментов
1. Airflow + PostgersSQL 


## ПО, включенное в сборку
### СУБД
* PostgreSQL
* MongoDB *todo*
### ETL
* Комплексные ETL | ELT
* * Airflow
* * Cronicle
* * Luigi *todo*
* * StreamSets *todo*
* E(xtract) *todo*
* T(ransform) *todo*
* * dbt *todo*
* L(oad) *todo*

### BI
* Metabase *todo*
* Superset *todo*

## Авторы
- Тимур Алейников - [iradio](https://github.com/iradio)