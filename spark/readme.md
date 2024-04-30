# SPARK

# Documentation

https://github.com/bitnami/bitnami-docker-spark

# Quick start
To run PySpark scripts you have to:
1. Start Spark with Spark worker using `docker-compose up --scale spark-worker=3 -d`.
2. Install PySpark on your local machine using `pip install pyspark`
3. Fix Spark requirements (install Java if it not installed yet). For example: `sudo apt-get install openjdk-8-jdk`

Execute your `.py` script on `Spark` using bash command: 
``` bash
spark-submit --master spark://localhost:8400 hello-spark-world.py
```