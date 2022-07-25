# SPARK

# Documentation

https://github.com/bitnami/bitnami-docker-spark

# Quick start
To run PySpark scripts you have to:
1. Start Spark with Spark worker using any `docker-composes_*spark*.yml`.
2. Install PySpark on your local machine using `pip install pyspark`
3. Fix Spark requirements (install Java if it not installed yet). For example: `sudo apt-get install openjdk-8-jdk`

Execute your `.py` script on `Spark` using bash command: 
``` bash
spark-submit --master spark://localhost:8080 spark/hello-spark-world.py
```