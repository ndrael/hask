import requests
import re
import json

R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"
C = "\033[1;36m"
W = "\033[1;37m"
N = "\033[0m"

def run(username):
    # Coba handle: @username, username biasa, atau URL channel
    username = username.lstrip('@')
    
    url = f"https://www.youtube.com/@{username}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36"
    }
    
    try:
        r = requests.get(url, headers=headers, timeout=10)
        
        if r.status_code == 404 or "This page isn't available" in r.text:
            # Coba tanpa @
            url = f"https://www.youtube.com/c/{username}"
            r = requests.get(url, headers=headers, timeout=10)
            
        if r.status_code == 404:
            print(f"{R}[-] Channel not found{N}")
            return
        
        html = r.text
        
        # Ambil subscriber count dari meta tag atau script
        subs = "N/A"
        videos_count = "N/A"
        channel_name = username
        description = "N/A"
        
        # Cari subscriber count
        subs_match = re.search(r'"subscriberCountText":\{"simpleText":"([^"]+)"', html)
        if not subs_match:
            subs_match = re.search(r'(\d+[\.,]?\d*[KMB]?) subscribers', html)
        if subs_match:
            subs = subs_match.group(1)
        
        # Cari channel name
        name_match = re.search(r'<title>(.+?) - YouTube</title>', html)
        if name_match:
            channel_name = name_match.group(1)
        
        # Cari description
        desc_match = re.search(r'"description":"([^"]+)"', html)
        if desc_match:
            description = desc_match.group(1).replace('\\n', '\n').replace('\\"', '"')
        
        # Coba ambil dari ytInitialData
        yt_match = re.search(r'var ytInitialData = ({.+?});</script>', html)
        if yt_match:
            try:
                yt_data = json.loads(yt_match.group(1))
                # Navigasi ke data channel
                header = yt_data.get("header", {}).get("c4TabbedHeaderRenderer", {})
                if header:
                    subs = header.get("subscriberCountText", {}).get("simpleText", subs)
                    channel_name = header.get("title", channel_name)
                    videos_count = header.get("videosCountText", {}).get("runs", [{}])[0].get("text", "N/A")
            except:
                pass
        
        print(f"{G}[+] Channel    : {channel_name}{N}")
        print(f"{G}[+] Username   : @{username}{N}")
        print(f"{G}[+] Subscribers: {subs}{N}")
        print(f"{G}[+] Videos     : {videos_count}{N}")
        print(f"{G}[+] Description: {description}{N}")
        print(f"{G}[+] Profile    : {url}{N}")
        
    except Exception as e:
        print(f"{R}[!] Error: {e}{N}")
