import requests, re, json

R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"
N = "\033[0m"

def run(username):
    username = username.lstrip('@')
    url = f"https://www.youtube.com/@{username}"
    headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36"}
    try:
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code == 404:
            print(f"{R}[-] Channel not found{N}")
            return
        html = r.text
        subs = "N/A"
        channel_name = username
        # Coba ambil dari ytInitialData
        yt_match = re.search(r'var ytInitialData = ({.+?});</script>', html)
        if yt_match:
            try:
                yt_data = json.loads(yt_match.group(1))
                header = yt_data.get("header", {}).get("c4TabbedHeaderRenderer", {})
                if header:
                    subs = header.get("subscriberCountText", {}).get("simpleText", "N/A")
                    channel_name = header.get("title", channel_name)
            except:
                pass
        print(f"{G}[+] Channel    : {channel_name}{N}")
        print(f"{G}[+] Username   : @{username}{N}")
        print(f"{G}[+] Subscribers: {subs}{N}")
        print(f"{G}[+] Profile    : {url}{N}")
    except Exception as e:
        print(f"{R}[!] Error: {e}{N}")
