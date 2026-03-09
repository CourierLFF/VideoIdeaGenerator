import requests
import os
from dotenv import load_dotenv

load_dotenv()

CURSEFORGE_API_KEY = os.getenv("CURSEFORGE_API_KEY")

def fetch_featured_curseforge(gameId: int):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'x-api-key': CURSEFORGE_API_KEY
    }

    body = {
        "gameId": gameId,
    }

    r = requests.post('https://api.curseforge.com/v1/mods/featured', headers = headers, json = body)
    jsonDataResponse = r.json()['data']['featured']

    return jsonDataResponse

def fetch_popular_curseforge(gameId: int, classId: int=4471):
    headers = {
        'Accept': 'application/json',
        'x-api-key': CURSEFORGE_API_KEY
    }

    if gameId == 432:
        r = requests.get('https://api.curseforge.com/v1/mods/search', params={
            'gameId': gameId,
            'classId': classId,
            'sortField': 'popularity',
            'sortOrder': 'desc'
        }, headers = headers)
    else:
        r = requests.get('https://api.curseforge.com/v1/mods/search', params={
            'gameId': gameId,
            'sortField': 'popularity',
            'sortOrder': 'desc'
        }, headers = headers)

    return r.json()['data']