from datetime import datetime

# Search Queries
QUERY = "pokemon"
MAX_RESULTS = 10
ORDER = "date"

# DAG Details
START_DATE = datetime(2021, 1, 1)
SCHEDULE_INTERVAL = "@daily"
CATCHUP = False
