from googleapiclient.discovery import build
from dotenv import load_dotenv
import os
import json
from defaults import (
    QUERY,
    MAX_RESULTS,
    ORDER,
)

load_dotenv()

YOUTUBE_API_KEY = os.environ["YOUTUBE_API_KEY"]


def youtube_authenticate_api_key(
    api_service_name,
    api_version,
    api_key,
):

    return build(api_service_name, api_version, developerKey=api_key)


def search(
    youtube,
    **kwargs,
):
    return youtube.search().list(
        part="snippet",
        **kwargs
    ).execute()


def youtube_extractor():

    api_key = YOUTUBE_API_KEY

    api_service_name = "youtube"
    api_version = "v3"

    youtube = youtube_authenticate_api_key(
        api_service_name,
        api_version,
        api_key,
    )

    kwargs = {
        'q': QUERY,
        'maxResults': MAX_RESULTS,
        'order': ORDER,
    }

    data = search(
        youtube,
        **kwargs,
    )

    with open("./youtube.json", 'w') as f:

        f.write(
            json.dumps(
                data,
                indent=4,
            )
        )

    return
