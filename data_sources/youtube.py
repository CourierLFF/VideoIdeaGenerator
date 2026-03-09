from googleapiclient.discovery import build
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
from utils import extract_cf_and_modrinth_urls

load_dotenv()

youtube = build('youtube', 'v3', developerKey=os.getenv("YOUTUBE_API_KEY"))

def search_popular_videos(query: str):

    one_week_ago = (datetime.utcnow() - timedelta(days=7)).isoformat("T") + "Z"

    request = youtube.search().list(
        part='snippet',
        q=query,
        type='video',
        order='viewCount',
        relevanceLanguage='en',
        regionCode='US',
        publishedAfter=one_week_ago,
        maxResults=15
    )
    response = request.execute()
    return response['items']

def get_links_from_channel(channel_ids: list[str]):
    links = []
    for channel_id in channel_ids:
        ch_request = youtube.channels().list(
            part='contentDetails',
            id=channel_id
        )
        ch_response = ch_request.execute()
        uploads_playlist_id = ch_response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

        pl_request = youtube.playlistItems().list(
            part='snippet',
            playlistId=uploads_playlist_id,
            maxResults=20
        )
        pl_response = pl_request.execute()

        for item in pl_response['items']:
            description = item['snippet']['description']
            found_urls = extract_cf_and_modrinth_urls(description)
            if found_urls:
                links.extend(found_urls)
    
    return links