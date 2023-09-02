from airflow import DAG
from airflow.operators.python import PythonOperator
 
from airflow.operators.postgres_operator import PostgresOperator

from datetime import datetime

from extract import youtube_extractor
from transform import youtube_transform
from load import youtube_load

from defaults import (
    START_DATE,
    SCHEDULE_INTERVAL,
    CATCHUP,
)


with DAG(
    "youtube_etl",
    start_date=START_DATE,
    schedule_interval=SCHEDULE_INTERVAL,
    catchup=CATCHUP,
    template_searchpath='opt/airflow/dags',
) as dag:

    create_table = PostgresOperator(
        task_id='create_table',
        postgres_conn_id='postgres_local',
        sql='create_table.sql'
    )

    extract = PythonOperator(
        task_id="extract_youtube",
        python_callable=youtube_extractor,
    )

    transform = PythonOperator(
        task_id="transform_youtube",
        python_callable=youtube_transform,
    )

    load = PythonOperator(
        task_id="load_youtube",
        python_callable=youtube_load,
    )

    create_table >> extract >> transform >> load
