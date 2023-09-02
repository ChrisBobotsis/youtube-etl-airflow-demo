from typing import Dict, Any
import pandas as pd
import json


def youtube_transform():

    # data = ti.xcom_pull(task_ids=["extract_youtube"])

    with open("./youtube.json", 'r') as f:

        data = json.load(f)

    transformed_data = []

    for video in data["items"]:

        x = {}

        x["id"] = video["id"]["videoId"]

        x["type"] = video["id"]["kind"]

        x["published_at"] = video["snippet"]["publishedAt"]

        x["channel"] = video["snippet"]["channelTitle"]

        x["title"] = video["snippet"]["title"]

        x["description"] = video["snippet"]["description"]

        transformed_data.append(x)

    df = pd.DataFrame.from_dict(transformed_data)

    df.to_csv(
        "./youtube.csv",
        index=False,
        header=False,
        sep='\t'
    )

    return


if __name__ == "__main__":

    with open("./youtube.json", 'r') as f:

        data = json.load(f)

    x = youtube_transform()

    import pdb; pdb.set_trace()
