# DAGSTER

Based on https://docs.dagster.io/deployment/guides/docker#example

# How to run 
1. Create virtual env with python 3.9  
``` bash
cd dagster
python3.9 -m venv venv
source venv/bin/activate
python --version
```
You should see something like:  
``` bash
(venv) usrname@pc:/path/to/de-toolkit/dagster$ python --version
Python 3.9.13
```

2. Install Dagster  
``` bash
pip install dagster dagit
dagster new-project tutorial

```

3. Run Dagster
``` bash
cd tutorial/
pip install --editable .
dagit
```
Result: dagit server starts on http://localhost:3000/

3. Start Dagster Daemon  
start new console and activate venv
``` bash
cd dagster
source venv/bin/activate
export DAGSTER_HOME=/path/to/de-toolkit/dagster/daemon
cd ./dagster/tutorial
dagster-daemon run
```
Result: Dagster daemon starts locally

4. Run tests
start new console and activate venv
``` bash
cd dagster
source venv/bin/activate
pytest tutorial_tests
```

# Tutorial 
https://docs.dagster.io/tutorial


