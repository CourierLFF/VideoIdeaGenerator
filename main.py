from data_analyzer import analyze_curseforge, count_duplicate_links, export_data_to_file, gather_data, analyze_youtube_links
from data_sources.curseforge import fetch_featured_curseforge, fetch_popular_curseforge
from data_sources.youtube import get_links_from_channel, search_popular_videos
from prompter import prompt_for_videos
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
    
    analyzed_curseforge_featured_minecraft = analyze_curseforge(datajson['featuredCurseForgeMinecraft'])
    analyzed_curseforge_featured_hytale = analyze_curseforge(datajson['featuredCurseForgeHytale'])

    duplicate_links_minecraft = count_duplicate_links(datajson['minecraft_links'])
    duplicate_links_hytale = count_duplicate_links(datajson['hytale_links'])

    video_titles = prompt_for_videos(json.dumps(analyzed_curseforge_featured_minecraft, indent=2), json.dumps(analyzed_curseforge_featured_hytale, indent=2), json.dumps(duplicate_links_minecraft, indent=2), json.dumps(duplicate_links_hytale, indent=2))
    print(video_titles)
