from dagster import  op, graph, Out, In, Output, Nothing
from dagster import asset, DailyPartitionsDefinition
from datetime import date

import psycopg2
import os
import pandas as pd

postgres_connection = {"host":"rc1b-w5d285tmxa8jimyn.mdb.yandexcloud.net","port":"6432","user":"student","password":"de_student_112022","database":"db1"}
# partitions_def = DailyPartitionsDefinition(start_date="2022-10-01")

@asset
def extract_currencies():
    # достаем дату запуска DAG и сдвигаем на -1 день для извлечения данных за "вчера"
    # execution_date = (context['logical_date'] - timedelta(days=1) ).strftime('%Y-%m-%d') 
    # logger.info(f"Execution date is {execution_date}")

    # conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
    conn = psycopg2.connect(**postgres_connection)
    cur = conn.cursor()
    
    batch_size = 10000
    offset = 0
    rest = 1
    results = []
    while rest != 0 :

        # Execute the query to select all rows from the table
        select_sql = f"SELECT * FROM public.currencies LIMIT {batch_size} OFFSET {offset}"
        logger.info(f"SQL satement: {select_sql}")
        cur.execute(select_sql)

        # Fetch all rows from the query result
        rows = cur.fetchall()
        rest = len(rows)
        logger.info(f"rows: {rest}")
        if rest == 0:
            break
        results.append(rows)
        filepath = f"{tmp_dir_path}/stg_{table_name}_{execution_date}_{offset // batch_size}.csv"
        
        # Write the data to a CSV file
        # with open(filepath, 'w', newline='') as csvfile:
        #     writer = csv.writer(csvfile)
        #     writer.writerow([i[0] for i in cur.description])  # Write the header row
        #     for row in rows:
        #         writer.writerow(row)
        #     files.append(filepath)        

        # increment offset
        offset += batch_size

    # Close the cursor and database connection
    cur.close()
    conn.close()
    return pd.DataFrame(results)
    # logger.info(f"Files: {files}")
    # context['ti'].xcom_push(key=f'files_{table_name}_{execution_date}', value=json.dumps(files))