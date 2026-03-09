from data_sources.curseforge import fetch_featured_curseforge

if __name__ == "__main__":
    featuredCurseforge = fetch_featured_curseforge(70216)
    for mod in featuredCurseforge:
        print(mod['links']['websiteUrl'])