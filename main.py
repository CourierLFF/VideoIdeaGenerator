from data_sources.curseforge import fetch_featured_curseforge, fetch_popular_curseforge

# GAME IDs
# Minecraft = 432
# Hytale = 70216

# Class IDs
# Modpacks = 4471
# Mod = 6
# Resource Pack = 12
# World = 17

if __name__ == "__main__":
    CurseForgeModpacks = fetch_popular_curseforge(432)
    for modpack in CurseForgeModpacks:
        print(modpack['name'])
    