#!/usr/bin/env python3
# HASK - Hybrid Attack & Spy Kernel
# Author: ndrael
import os, sys, time

R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"
C = "\033[1;36m"
W = "\033[1;37m"
N = "\033[0m"

BANNER = f"""
{G} _  _   _   ___ _  __
| || | /_\\ / __| |/ /
| __ |/ _ \\\\__ \\ ' < 
|_||_/_/ \\_\\___/_|\\_\\{W} by: ndrael{N}
"""

MODULES_DIR = "modules"

def load_modules():
    modules = {}
    for category in ["attack", "spy"]:
        cat_path = os.path.join(MODULES_DIR, category)
        if os.path.exists(cat_path):
            for file in os.listdir(cat_path):
                if file.endswith(".py") and file != "__init__.py":
                    name = file[:-3]
                    try:
                        mod = __import__(f"{MODULES_DIR}.{category}.{name}", fromlist=["run", "DESCRIPTION"])
                        modules[name] = mod
                    except Exception as e:
                        pass
    return modules

def show_main():
    os.system("clear")
    print(BANNER)
    print(f"  {W}Tools   = HASK{N}")
    print(f"  {W}Version = 0.1 (beta){N}\n")
    print(f"  {W}[*] Type /menu for command list{N}")

def show_menu():
    print(f"""
  {R}┌─ ATTACK:{N}
  {R}│{N} {W}/ddos          = DDoS flood multi-source{N}
  {R}│{N} {W}/sqli          = SQL injection auto exploit{N}
  {R}│{N} {W}/spam          = SMS verification exploit (multi-platform){N}

  {Y}┌─ SPY:{N}
  {Y}│{N} {W}/server        = Server info & port scanner{N}
  {Y}│{N} {W}/stalk         = Username social media tracker{N}
  {Y}│{N} {W}/web           = Website vulnerability info{N}

  {C}┌─ SYSTEM:{N}
  {C}│{N} {W}/menu          = Show command list{N}
  {C}│{N} {W}/help          = Contact support{N}
  {C}│{N} {W}/clear         = Clear screen{N}
  {C}│{N} {W}/exit          = Exit HASK{N}
""")

def show_help():
    print(f"""
  {W}Contact support:{N}
  Email: ndrael.org@gmail.com
""")

def main():
    show_main()
    modules = load_modules()

    while True:
        try:
            cmd = input(f"\n{W}┌─[hask]─[~]\n└──╼ > {N}").strip().lower()
        except (KeyboardInterrupt, EOFError):
            print(f"\n{R}[!] Exiting...{N}")
            sys.exit(0)

        if cmd in ["/exit", "exit"]:
            print(f"{R}[!] Shutting down...{N}")
            time.sleep(0.5)
            sys.exit(0)
        elif cmd == "/clear":
            show_main()
        elif cmd == "/menu":
            show_menu()
        elif cmd == "/help":
            show_help()
        elif cmd.startswith("/"):
            cmd_name = cmd[1:]
            if cmd_name in modules:
                try:
                    modules[cmd_name].run()
                except Exception as e:
                    print(f"{R}[!] Error: {e}{N}")
            else:
                print(f"{R}[!] Unknown command. Type /menu{N}")
        else:
            print(f"{R}[!] Use '/' prefix. Example: /menu{N}")

if __name__ == "__main__":
    main()
