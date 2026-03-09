from data_sources.curseforge import fetch_featured_curseforge, fetch_popular_curseforge
from data_sources.youtube import get_links_from_channel, search_popular_videos
import os
from dotenv import load_dotenv

load_dotenv()

# GAME IDs
# Minecraft = 432
# Hytale = 70216

# Class IDs
# Modpacks = 4471
# Mod = 6
# Resource Pack = 12
# World = 17

if __name__ == "__main__":
    minecraft_channel_ids = os.getenv("MINECRAFT_YOUTUBE_CHANNEL_IDS").split(",")
    hytale_channel_ids = os.getenv("HYTALE_YOUTUBE_CHANNEL_IDS").split(",")
    description_data = get_links_from_channel(hytale_channel_ids)
    print(description_data)
    