import requests

R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"
N = "\033[0m"

def run(username):
    url = f"https://www.tiktok.com/@{username}"
    headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36"}
    try:
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code == 404:
            print(f"{R}[-] User not found{N}")
            return
        print(f"{G}[+] Username  : @{username}{N}")
        print(f"{G}[+] Profile   : {url}{N}")
        print(f"{Y}[~] Full data extraction requires further parsing.{N}")
    except Exception as e:
        print(f"{R}[!] Error: {e}{N}")
