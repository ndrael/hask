import requests

R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"
N = "\033[0m"

def run(username):
    url = f"https://api.github.com/users/{username}"
    headers = {"User-Agent": "HASK/0.1"}
    try:
        r = requests.get(url, headers=headers, timeout=5)
        if r.status_code == 404:
            print(f"{R}[-] User not found{N}")
            return
        data = r.json()
        print(f"{G}[+] Username  : {data.get('login', 'N/A')}{N}")
        print(f"{G}[+] Name      : {data.get('name', 'N/A')}{N}")
        print(f"{G}[+] Bio       : {data.get('bio', 'N/A')}{N}")
        print(f"{G}[+] Followers : {data.get('followers', 0)}{N}")
        print(f"{G}[+] Following : {data.get('following', 0)}{N}")
        print(f"{G}[+] Repos     : {data.get('public_repos', 0)}{N}")
        print(f"{G}[+] Profile   : https://github.com/{username}{N}")
    except Exception as e:
        print(f"{R}[!] Error: {e}{N}")
