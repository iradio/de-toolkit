ARG JUPYTER_BASE
ARG JUPYTER_BASE_VERSION

FROM jupyter/${JUPYTER_BASE:-pyspark-notebook}:${JUPYTER_BASE_VERSION:-latest}

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt