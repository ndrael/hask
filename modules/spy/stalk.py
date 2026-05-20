import os, sys, importlib

DESCRIPTION = "Username social media tracker"

R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"
C = "\033[1;36m"
W = "\033[1;37m"
N = "\033[0m"

STALK_DIR = os.path.join(os.path.dirname(__file__), "stalk")

def load_platforms():
    platforms = {}
    if os.path.exists(STALK_DIR):
        for file in os.listdir(STALK_DIR):
            if file.endswith(".py") and file != "__init__.py":
                name = file[:-3]
                try:
                    spec = importlib.util.spec_from_file_location(
                        f"modules.spy.stalk.{name}",
                        os.path.join(STALK_DIR, file)
                    )
                    mod = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(mod)
                    platforms[name] = mod
                except Exception as e:
                    pass
    return platforms

def show_stalk_menu(platforms):
    print(f"""
  {Y}┌─ STALK MENU:{N}
  {Y}│{N}""")
    
    keys = list(platforms.keys())
    for i, name in enumerate(keys, 1):
        display = name.capitalize()
        print(f"  {Y}│{N} {W}[{i}] {display}{N}")
    
    print(f"""  {Y}│{N}
  {Y}│{N} {W}[A]  Scan ALL platforms{N}
  {Y}│{N} {W}[B]  Back to main menu{N}""")

def run():
    platforms = load_platforms()
    
    if not platforms:
        print(f"{R}[!] No platform modules found in stalk/{N}")
        input(f"{Y}[*] Press Enter to continue...{N}")
        return
    
    username = input(f"{Y}[?] Target username: {N}")
    
    while True:
        show_stalk_menu(platforms)
        choice = input(f"{Y}[?] Select platform: {N}").strip().upper()
        
        if choice == "B":
            print(f"{G}[*] Back to main menu.{N}")
            break
        elif choice == "A":
            print(f"\n{C}[*] Scanning ALL platforms for '{username}'...{N}\n")
            for name, mod in platforms.items():
                print(f"{C}─── {name.capitalize()} ───{N}")
                try:
                    mod.run(username)
                except Exception as e:
                    print(f"{R}[!] Error: {e}{N}")
                print()
            input(f"{Y}[*] Press Enter to continue...{N}")
        else:
            try:
                idx = int(choice) - 1
                keys = list(platforms.keys())
                if 0 <= idx < len(keys):
                    name = keys[idx]
                    print(f"\n{C}─── {name.capitalize()} ───{N}")
                    try:
                        platforms[name].run(username)
                    except Exception as e:
                        print(f"{R}[!] Error: {e}{N}")
                    input(f"\n{Y}[*] Press Enter to continue...{N}")
                else:
                    print(f"{R}[!] Invalid choice.{N}")
            except ValueError:
                print(f"{R}[!] Invalid choice.{N}")
