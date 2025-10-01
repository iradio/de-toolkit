# Spark

## Documentation

https://github.com/bitnami/bitnami-docker-spark

## Quick start
To run PySpark scripts:
1. Start Spark with additional workers: `docker-compose up --scale spark-worker=3 -d`.
2. Install PySpark locally: `pip install pyspark`.
3. Install the required JVM if it is not already available. For example: `sudo apt-get install openjdk-8-jdk`.

Run your `.py` script on Spark with:
```bash
spark-submit --master spark://localhost:8400 hello-spark-world.py
```
