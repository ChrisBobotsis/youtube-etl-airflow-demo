# youtube-etl-airflow-demo
This repository is a demo for how you can extract, load, and transform (ETL) data from youtube into a postgres database using Airflow.

[![alt text](/images/airflow_etl.png " ")](/images/airflow_etl.png)

## Setting Up

We need to create the appropriate directories and environmental variables:

```
mkdir -p ./dags ./logs ./plugins ./config

echo -e "AIRFLOW_UID=$(id -u)" > .env
```

Setting the `AIRFLOW_UID` to your user id ensures you will be able to access the files created in the previous folders.

## Add Youtube API Key

We need a [Youtube API](https://developers.google.com/youtube/v3/getting-started) in order to extract the data.

Once you have your API key, add it to your `.env` file.

```
echo -e YOUTUBE_API_KEY=<api_key> >> .env
```

## Selecting Search Criteria

You can alter the search criteria including the query, number of results and how to order the results by altering the constants in `defaults.py`.

Currently, these are the defaults:

```
QUERY = "pokemon"
MAX_RESULTS = 10
ORDER = "date"
```

## Selecting DAG Criteria

You can also alter the schedule of the DAG to perform this Youtube ETL by altering the values specified in `defaults.py`.

Currently these are the defaults:

```
START_DATE = datetime(2021, 1, 1)
SCHEDULE_INTERVAL = "@daily"
CATCHUP = False
```

## Initialize the Database

Need to run database migrations and create the first user account:

```
docker compose up airflow-init
```

The account created has the login `airflow` and the password `airflow`.

## Running Airflow

You can start all of the services required for airflow by running the following command:

```
docker compose up --build
```

We are adding the build argument here as we are using a custom image.

## Adding the Postgres Connection

Next you need to add the connection to the Postgres database.

Open a web browser and go to `localhost:8080`. The username and password are both `airflow`.

Navigate to the `Admins -> Connections` page.

Click the + button and add the following:

```
Connection Id:      postgres_local
Connection Type:    Postgres
Host:               postgres
Login:              airflow
Password:           airflow
Port:               5432
```

Then click save.

## Running a DAG

If you want to run the DAG outside of the schedule, you can navigate to the `localhost:8080/home` to view all of the DAGs.

There, you should see the `youtube_etl` DAG.

[![alt text](/images/airflow_dags.png " ")](/images/airflow_dags.png)

Unpause the DAG and Trigger it:

[![alt text](/images/unpause_dag.png " ")](/images/unpause_dag.png)

[![alt text](/images/trigger_dag.png " ")](/images/trigger_dag.png)

Then if you click on `youtube_etl` you can see the process:

[![alt text](/images/dag_graph.png " ")](/images/dag_graph.png)

## Accessing the Database

One way to access the database is to connect to the Postgres container and then connect to the Postgres database itself.

```
docker exec -ti <container id of postgres> /bin/bash
```

After we enter the container, we can access the database:

```
psql -U airflow
```

Then you can access the youtube data via the youtube table:

```
SELECT * FROM youtube LIMIT 5;
```

```
id |     type      |                                                  title                                                  |                                                       description                                                       |   videoid   | created_at |      channel       
----+---------------+---------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+-------------+------------+--------------------
  1 | youtube#video | LAST Pokemon Card Set of 2023, Paradox Rift, Secret Rares Revealed!                                     | LAST Pokemon Card Set of 2023, Paradox Rift, Secret Rares Revealed! Check out Drip Here!                                | Xx94FC1IFrs | 2023-09-02 | Dr. Applesauce Two
  2 | youtube#video | Ranking Your Pokémon Card Collections                                                                   | i am addicted to pokemon cards and plushes Marvel Snap is out on Steam! Download today using my link: ...               | -9PqwA8uBek | 2023-09-02 | Purplecliffe
  3 | youtube#video | Missed it by an evolution! | Who&#39;s That Pokemon #Shorts #Pokemon #whosthatpokemon                   | Watch Avghans live on Twitch: Avghans | https://www.twitch.tv/avghans Twitter | https://twitter.com/Avghans YouTube ... | 5vWnKe2X31E | 2023-09-02 | Avghans
  4 | youtube#video | The STRANGEST Items in Pokemon                                                                          | These are some of the strangest items in the Pokemon games! ——————————————— Become A Member: ...                        | IuUh7YWqXgo | 2023-09-02 | TerraQuake
  5 | youtube#video | ALL 114+ LEAKED RETURNING DLC POKEMON FOR THE TEAL MASK! FULL POKEDEX UPDATED! Scarlet &amp; Violet DLC | All 114+ returning Pokemon for the Teak Mask DLC in Scarlet & Violet have been LEAKED! These Pokemon have all been ...  | 1sxGUsMVi6A | 2023-09-02 | HDvee
(5 rows)
```

# Cleaning Up

The following command will stop and delete containers, delete volumes with database data and downloaded images:

```
docker compose down --volumes --rmi all
```


