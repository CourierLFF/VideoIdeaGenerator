import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()


def prompt_for_videos(mc_featured, hytale_featured, minecraft_links, hytale_links):
    message = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=1024,
        messages = [
            {"role": "user", 
            "content": f"Here is some data about the featured section of CurseForge for Minecraft: {mc_featured}, and here is a similar dataset for Hytale: {hytale_featured}. Additionally, here are the most frequently mentioned CurseForge links in Minecraft YouTube videos: {minecraft_links}, and here are the same for Hytale: {hytale_links}. Based on this data, can you suggest some video ideas that would be interesting to make for a YouTube channel focused on Minecraft and Hytale content? The channel is mostly focused on tutorials and showcases. No let's plays or things in a similar context. Give me about 20 titles or so. Do not give any extra information in your response other than the titles and small explanations for the titles. This is an example of one that looks good: '**Testing 10 Underrated Mods Under 50K Downloads** - Feature hidden gems like Traveler Tool Belt, Kaleidoscope Tavern, TVCraft'. You do not need to use that example exactly, just use a format that looks relatively similar to that. Focus mostly on mods / modpacks / other content that has a high amount of downloads or a high amount of links from the given data, content that has less downloads and less links should not be as prioritized. Do not include any kind of strategy tips or anything like that, just the titles and small explanations for the titles. Split your response into two sections, one for Minecraft and one for Hytale."},
        ]
    )

    return (message.content[0].text)