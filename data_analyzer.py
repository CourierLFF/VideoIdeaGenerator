import os
import json
from dotenv import load_dotenv
from data_sources.curseforge import fetch_featured_curseforge, fetch_popular_curseforge
from data_sources.youtube import get_links_from_channel
from utils import extract_name_from_url

load_dotenv()


def gather_data():
    minecraft_channel_ids = os.getenv("MINECRAFT_YOUTUBE_CHANNEL_IDS").split(",")
    hytale_channel_ids = os.getenv("HYTALE_YOUTUBE_CHANNEL_IDS").split(",")

    featuredCurseForgeMinecraft = fetch_featured_curseforge(432)
    featuredCurseForgeHytale = fetch_featured_curseforge(70216)

    popularCurseForgeMinecraftModpacks = fetch_popular_curseforge(432, 4471)
    popularCurseForgeMinecraftMods = fetch_popular_curseforge(432, 6)
    popularCurseForgeHytale = fetch_popular_curseforge(70216)

    minecraft_links = get_links_from_channel(minecraft_channel_ids)
    hytale_links = get_links_from_channel(hytale_channel_ids)

    return {
        "featuredCurseForgeMinecraft": featuredCurseForgeMinecraft,
        "featuredCurseForgeHytale": featuredCurseForgeHytale,
        "popularCurseForgeMinecraftModpacks": popularCurseForgeMinecraftModpacks,
        "popularCurseForgeMinecraftMods": popularCurseForgeMinecraftMods,
        "popularCurseForgeHytale": popularCurseForgeHytale,
        "minecraft_links": minecraft_links,
        "hytale_links": hytale_links
    }

def analyze_curseforge(data):
    important_info = {}
    for entry in data:
        important_info[entry['name']] = {
            "url": entry['links']['websiteUrl'],
            "downloads": entry['downloadCount'],
        }
    return important_info

def analyze_youtube_links(links):
    names = [extract_name_from_url(link) for link in links]
    for i, name in enumerate(names):
        names[i] = name.replace("-", " ").title()

    names_and_links = {name: link for name, link in zip(names, links)}
    return names_and_links

def count_duplicate_links(links):
    duplicate_dict = {}
    for link in links:
        if link in duplicate_dict:
            duplicate_dict[link] += 1
        else:
            duplicate_dict[link] = 1
    return sorted(duplicate_dict.items(), key=lambda x: x[1], reverse=True)



def export_data_to_file(data, filename="data.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)