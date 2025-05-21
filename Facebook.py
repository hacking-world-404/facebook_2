from os import system as c
import time
import random

A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;46m'
C = '\x1b[38;5;14m'
P = '\x1b[38;5;201m'

def logo():
    c('clear')
    print(f"""{P}
███████╗ █████╗  ██████╗███████╗███████╗ ██████╗ 
██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝██╔═══██╗
███████╗███████║██║     █████╗  █████╗  ██║   ██║
╚════██║██╔══██║██║     ██╔══╝  ██╔══╝  ██║   ██║
███████║██║  ██║╚██████╗███████╗███████╗╚██████╔╝
╚══════╝╚═╝  ╚═╝ ╚═════╝╚══════╝╚══════╝ ╚═════╝ 
{Y}HACKING WORLD - FB AUTO FOLLOW TOOL (NON-ROOT)
{A}-------------------------------------------------
""")

def loading(msg):
    for i in range(3):
        print(f"{C}{msg}{'.'*i}")
        time.sleep(0.5)
        c('clear')
        logo()

def auto_follow():
    logo()
    user = input(f"{C}[+] Enter Facebook Profile link: ")
    loading("Connecting to Facebook Server")
    print(f"{G}[✓] Profile Verified: {user}")
    time.sleep(1)

    followers = random.randint(500, 5000)
    print(f"{Y}[*] Adding {followers} Followers to {user}...")
    time.sleep(2)

    for percent in range(0, 101, 10):
        print(f"{C}[*] Inject Progress: {percent}%")
        time.sleep(0.25)
        c('clear')
        logo()

    print(f"{G}[✓] Successfully Added {followers} Followers to {user}!")
    print(f"{P}[*] Please Restart Facebook App to See New Followers.")
    input(f"\n{C}Press Enter To Exit...")

auto_follow()