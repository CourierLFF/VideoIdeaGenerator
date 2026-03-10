import re

def extract_cf_and_modrinth_urls(text: str):
    url_pattern = r'(https?://(?:www\.)?(?:curseforge\.com|modrinth\.com)/[^\s]+)'
    urls = re.findall(url_pattern, text)
    return urls

def extract_name_from_url(url: str):
    match = re.search(r'[^/]+$', url)
    if match:
        return match.group(0)
    return None