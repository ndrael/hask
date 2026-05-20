import requests

R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"
N = "\033[0m"

def run(username):
    url = f"https://www.instagram.com/{username}/?__a=1&__d=1"
    headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36"}
    try:
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code == 404:
            print(f"{R}[-] User not found{N}")
            return
        try:
            user = r.json()["graphql"]["user"]
        except:
            print(f"{Y}[~] API blocked or changed. Try again later.{N}")
            return
        print(f"{G}[+] Username  : {user.get('username', 'N/A')}{N}")
        print(f"{G}[+] Full Name : {user.get('full_name', 'N/A')}{N}")
        print(f"{G}[+] Bio       : {user.get('biography', 'N/A')}{N}")
        print(f"{G}[+] Verified  : {user.get('is_verified', False)}{N}")
        print(f"{G}[+] Private   : {user.get('is_private', False)}{N}")
        print(f"{G}[+] Posts     : {user.get('edge_owner_to_timeline_media', {}).get('count', 0)}{N}")
        print(f"{G}[+] Followers : {user.get('edge_followed_by', {}).get('count', 0)}{N}")
        print(f"{G}[+] Following : {user.get('edge_follow', {}).get('count', 0)}{N}")
        print(f"{G}[+] Profile   : https://www.instagram.com/{username}/{N}")
    except Exception as e:
        print(f"{R}[!] Error: {e}{N}")
