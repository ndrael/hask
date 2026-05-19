import requests

DESCRIPTION = "Website vulnerability info"

R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"
N = "\033[0m"

def run():
    url = input(f"{Y}[?] Target URL: {N}")
    
    if not url.startswith("http"):
        url = "http://" + url
    
    print(f"{G}[*] Scanning {url}...{N}\n")
    
    try:
        r = requests.get(url, timeout=5)
        print(f"{G}[+] Status: {r.status_code}{N}")
        
        # Server header
        server = r.headers.get("Server", "N/A")
        print(f"{G}[+] Server: {server}{N}")
        
        # X-Powered-By
        powered = r.headers.get("X-Powered-By", "N/A")
        print(f"{G}[+] Powered by: {powered}{N}")
        
        # Content-Type
        content_type = r.headers.get("Content-Type", "N/A")
        print(f"{G}[+] Content-Type: {content_type}{N}")
        
        # Check common paths
        paths = ["/admin", "/wp-admin", "/login", "/robots.txt", "/.git/", "/.env"]
        print(f"\n{Y}[*] Checking common paths...{N}")
        for path in paths:
            try:
                check = requests.get(url.rstrip("/") + path, timeout=3)
                if check.status_code != 404:
                    print(f"{Y}[~] {path} → {check.status_code}{N}")
            except:
                pass
                
    except:
        print(f"{R}[!] Cannot connect to {url}{N}")
