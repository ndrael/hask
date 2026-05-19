import requests

DESCRIPTION = "Username social media tracker"

R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"
N = "\033[0m"

PLATFORMS = {
    "GitHub": "https://github.com/{}",
    "Instagram": "https://www.instagram.com/{}/",
    "Twitter": "https://twitter.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "TikTok": "https://www.tiktok.com/@{}",
    "YouTube": "https://www.youtube.com/@{}",
    "Telegram": "https://t.me/{}",
}

def run():
    username = input(f"{Y}[?] Target username: {N}")
    print(f"{G}[*] Searching for '{username}' across platforms...{N}\n")
    
    for platform, url in PLATFORMS.items():
        try:
            r = requests.get(url.format(username), timeout=5)
            if r.status_code == 200:
                print(f"{G}[+] {platform}: Found → {url.format(username)}{N}")
            elif r.status_code == 404:
                print(f"{R}[-] {platform}: Not found{N}")
            else:
                print(f"{Y}[~] {platform}: Unknown ({r.status_code}){N}")
        except:
            print(f"{R}[!] {platform}: Error{N}")
