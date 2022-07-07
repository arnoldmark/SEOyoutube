from googleapiclient.discovery import build
import json
import os
import requests
import sqlalchemy as db
import pandas as pd

api_key = os.environ.get("ytapi_key")

youtube = build('youtube', 'v3', developerKey=api_key)



def get_playlistId():
  pl_id = input("Type or paste in the playlistID found in the url after the list and equals operator:")
  return pl_id


videos = []

pl_id = get_playlistId()

#pl_id = "PL1vwtZvNWlaYNGGlJs_G9sl6WTE2t27V2"
pl_request = youtube.playlistItems().list(
part='contentDetails',
playlistId=pl_id
)


pl_response = pl_request.execute()


vid_ids = []
for item in pl_response['items']:
  vid_ids.append(item['contentDetails']['videoId'])
vid_request = youtube.videos().list(
part="statistics",
id=','.join(vid_ids)
)

vid_response = vid_request.execute()

for item in vid_response['items']:
  vid_views = item['statistics']['viewCount']

vid_id = item['id']
yt_link = f'https://youtu.be/{vid_id}'

videos.append(
{
'views': int(vid_views),
'url': yt_link
}
)


videos.sort(key=lambda vid: vid['views'], reverse=True)
print(videos)
for video in videos[:10]:
#print(video['url'], video['views'])       

  def ytvid_stats(vid_response):
    try:
      pldata =  vid_response['items'][0]['statistics']   
      col_names =['url','views']
      pldata_Dataframe = pd.Dataframe(columns=col_names)
      engine = db.create_engine('sqlite:///dataYT.db')
      pldata_Dataframe.to_sql('pldata', con=engine, if_exists='replace', index=True)
      query_result = engine.execute("SELECT * FROM pl_data;").fetchall()
      print(pd.Dataframe(query_result))
    except :
      print("Sorry that video is not in the youtube database")      
      
