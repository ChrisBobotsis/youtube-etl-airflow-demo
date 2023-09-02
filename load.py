from airflow.hooks.postgres_hook import PostgresHook


def youtube_load():

    postgres_sql_upload = PostgresHook(postgres_conn_id="postgres_local")

    postgres_sql_upload.bulk_load(
        "youtube(videoId, type, created_at, channel, title, description)",
        "youtube.csv",
    )

    return True
