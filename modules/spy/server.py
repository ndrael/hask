import socket

DESCRIPTION = "Server info & port scanner"

R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"
N = "\033[0m"

COMMON_PORTS = [21, 22, 25, 53, 80, 110, 143, 443, 993, 995, 3306, 8080, 8443]

def run():
    target = input(f"{Y}[?] Target IP/domain: {N}")
    
    # Get IP
    try:
        ip = socket.gethostbyname(target)
        print(f"{G}[+] IP Address: {ip}{N}")
    except:
        print(f"{R}[!] Cannot resolve host{N}")
        return
    
    # Get hostname
    try:
        hostname = socket.gethostbyaddr(ip)[0]
        print(f"{G}[+] Hostname: {hostname}{N}")
    except:
        print(f"{G}[+] Hostname: N/A{N}")
    
    # Port scan
    print(f"{Y}[*] Scanning common ports...{N}")
    for port in COMMON_PORTS:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((ip, port))
            if result == 0:
                print(f"{G}[+] Port {port}: OPEN{N}")
            s.close()
        except:
            pass
    print(f"{G}[*] Scan complete.{N}")
