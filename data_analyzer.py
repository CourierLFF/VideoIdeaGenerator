import os
from dotenv import load_dotenv
from data_sources.curseforge import fetch_featured_curseforge, fetch_popular_curseforge
from data_sources.youtube import get_links_from_channel

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

