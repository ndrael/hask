import requests

R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"
C = "\033[1;36m"
W = "\033[1;37m"
N = "\033[0m"

def run(username):
    url = f"https://api.github.com/users/{username}"
    headers = {"User-Agent": "HASK/0.1"}
    
    try:
        r = requests.get(url, headers=headers, timeout=5)
        
        if r.status_code == 404:
            print(f"{R}[-] User not found{N}")
            return
        elif r.status_code != 200:
            print(f"{Y}[~] Status: {r.status_code}{N}")
            return
        
        data = r.json()
        
        print(f"{G}[+] Username  : {data.get('login', 'N/A')}{N}")
        print(f"{G}[+] Name      : {data.get('name', 'N/A')}{N}")
        print(f"{G}[+] Bio       : {data.get('bio', 'N/A')}{N}")
        print(f"{G}[+] Company   : {data.get('company', 'N/A')}{N}")
        print(f"{G}[+] Location  : {data.get('location', 'N/A')}{N}")
        print(f"{G}[+] Blog      : {data.get('blog', 'N/A')}{N}")
        print(f"{G}[+] Email     : {data.get('email', 'N/A')}{N}")
        print(f"{G}[+] Twitter   : {data.get('twitter_username', 'N/A')}{N}")
        print(f"{G}[+] Followers : {data.get('followers', 0)}{N}")
        print(f"{G}[+] Following : {data.get('following', 0)}{N}")
        print(f"{G}[+] Public Repos : {data.get('public_repos', 0)}{N}")
        print(f"{G}[+] Public Gists : {data.get('public_gists', 0)}{N}")
        print(f"{G}[+] Created   : {data.get('created_at', 'N/A')}{N}")
        print(f"{G}[+] Updated   : {data.get('updated_at', 'N/A')}{N}")
        print(f"{G}[+] Profile   : https://github.com/{username}{N}")
        
    except Exception as e:
        print(f"{R}[!] Error: {e}{N}")
