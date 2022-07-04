
import requests
import json
import os


#api_key = os.environ.get('ytapi_key')
api_key = 'AIzaSyBHJLFrB83J3C6NJkWTiPzVHOZjIydWjOc'
channel_Id = 'UC4tjY2tTltEKePusozUxtSA'

url = f'https://www.googleapis.com/youtube/v3/channels?part=contentDetails,statistics&id={channel_Id}&key={api_key}'

json_url = requests.get(url)

data = json.loads(json_url.text)
print(data)