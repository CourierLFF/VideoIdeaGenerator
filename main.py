from data_analyzer import analyze_curseforge, export_data_to_file, gather_data
from data_sources.curseforge import fetch_featured_curseforge, fetch_popular_curseforge
from data_sources.youtube import get_links_from_channel, search_popular_videos
import os
import json
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
    datajson = None
    with open("data.json", "r") as f:
        datajson = json.load(f)
    
    analyzed_data = analyze_curseforge(datajson["popularCurseForgeMinecraftModpacks"])
    print(analyzed_data)