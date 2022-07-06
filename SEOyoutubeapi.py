from googleapiclient.discovery import build
import json
import os
#import requests

api_key = os.environ.get("ytapi_key")

youtube = build('youtube', 'v3', developerKey=api_key)

channel_Id = "UCCezIgC97PvUuR4_gbFUs5g"
#'UC4tjY2tTltEKePusozUxtSA'
request = youtube.channels().list(
        part='statistics',
        id=channel_Id
    )

response = request.execute()

json_object = json.dumps(response, indent=4)
print(json_object)

#print(json_object('subscriberCounter'))

