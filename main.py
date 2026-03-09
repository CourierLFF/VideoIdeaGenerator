from data_sources.curseforge import fetch_featured_curseforge_minecraft

if __name__ == "__main__":
    featuredCurseforgeMinecraft = fetch_featured_curseforge_minecraft()
    print(featuredCurseforgeMinecraft)