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