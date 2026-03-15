import csv

def write_csv(analyzed_cf_mc, analyzed_cf_hy, duplicate_links_mc, duplicate_links_hy, video_titles):
    with open("test.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        titles_list = video_titles.split("\n\n")
        titles_rows = [["Video Titles"], 
                       ["Title"]] + \
                       [[title.strip()] for title in titles_list if title.strip()]
        
        for title_row in titles_rows:
            writer.writerow(title_row)

        writer.writerow([])
        writer.writerow([])  

        mc_forge_rows = [["Minecraft Featured CurseForge", "", ""],
                         ["Name", "URL", "Downloads"]] + \
                         [[name, data['url'], data['downloads']] for name, data in analyzed_cf_mc.items()]
        
        hy_forge_rows = [["Hytale Featured CurseForge", "", ""],
                         ["Name", "URL", "Downloads"]] + \
                         [[name, data['url'], data['downloads']] for name, data in analyzed_cf_hy.items()]

        duplicate_links_mc_rows = [["Minecraft YouTube Links", "", ""],
                                    ["Link", "Count"]] + \
                                    [[link, count] for link, count in duplicate_links_mc]
        
        duplicate_links_hy_rows = [["Hytale YouTube Links", "", ""],
                                    ["Link", "Count"]] + \
                                    [[link, count] for link, count in duplicate_links_hy]
        
        max_rows = max(len(mc_forge_rows), len(hy_forge_rows), len(duplicate_links_mc_rows), len(duplicate_links_hy_rows), len(titles_rows))

        mc_forge_rows += [["", "", ""]] * (max_rows - len(mc_forge_rows))
        hy_forge_rows += [["", "", ""]] * (max_rows - len(hy_forge_rows))
        duplicate_links_mc_rows += [["", ""]] * (max_rows - len(duplicate_links_mc_rows))
        duplicate_links_hy_rows += [["", ""]] * (max_rows - len(duplicate_links_hy_rows))
        titles_rows += [[""]] * (max_rows - len(titles_rows))

        for i in range(max_rows):
            row = mc_forge_rows[i] + ["", ""] + hy_forge_rows[i] + ["", ""] + duplicate_links_mc_rows[i] + ["", ""] + duplicate_links_hy_rows[i]
            writer.writerow(row)
