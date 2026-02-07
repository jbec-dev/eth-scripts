# --------------------------------------
# Wordlist Password Checker by jbec 2026
# --------------------------------------

# -> Uses the most popular wordlists! <-
# -> ! SecLists has to be installed ! <-

# -------------- Banner ----------------

BANNER = r"""
 __        __ _       _____ _           _
 \ \      / /| |     |  ___(_)_ __   __| | ___ _ __
  \ \ /\ / / | |_____| |_  | | '_ \ / _` |/ _ \ '__|
   \ V  V /  | |_____|  _| | | | | | (_| |  __/ |
    \_/\_/   |_|     |_|   |_|_| |_|\__,_|\___|_|

                [ wlFinder | Wordlist Password Checking Tool ]
"""
print(BANNER)

# -------------- Imports ---------------

import os
from termcolor import colored, cprint
from getpass import getpass

# -------------- Colours ---------------

MINT_GREEN = "\033[38;2;152;251;152m"  # light mint green (RGB)
PASTEL_BLUE = "\033[38;2;176;224;230m"  # powder blue

RESET = "\033[0m"

# ------------- Categories -------------
wordlists_common = ["100k-most-used-passwords-NCSC.txt", "xato-net-10-million-passwords.txt", "top-20-common-SSH-passwords.txt", ]
wordlists_time = ["seasons.txt", "months.txt", "days.txt"]
wordlists_default = ["default-passwords.txt", "ssh-betterdefaultpasslist.txt"]
wordlists_cracked = ["milw0rm-dictionary.txt"]
wordlists_general = ["darkc0de.txt", "openwall.net-all.txt"]



# ---------------- Main ----------------

# Check for SecLists

share = os.listdir("/usr/share")
for i in range(1):    
    if "seclists" in share:
        print(f"{MINT_GREEN}[+] SecLists found!{RESET}")
        continue
    else:
        cprint("Please install SecLists (sudo apt install seclists)!\n", "red")
        break

# Read user input to passw variable
passw = getpass(f"{PASTEL_BLUE}[I] Please enter the Password to check: {RESET}")

# check wordlists function
def checkfl(wl_array, wl_dir, passw_str):
    for i in range(len(wl_array)):
        found = False
        wl_file = f"{wl_dir}{wl_array[i]}"
        with open(wl_file, "r") as f:
            for line in f:
                if passw_str in line:
                    found = True
                    break
    if found == True:
        return True

# ---------- Check Wordlists -----------

common_check = checkfl(wordlists_common, "/usr/share/seclists/Passwords/Common-Credentials/", passw)
time_check = checkfl(wordlists_time, "/usr/share/seclists/Passwords/", passw)
default_check = checkfl(wordlists_default, "/usr/share/seclists/Passwords/Default-Credentials/", passw)
cracked_check = checkfl(wordlists_cracked, "/usr/share/seclists/Passwords/Cracked-Hashes/", passw)
general_check = checkfl(wordlists_general, "/usr/share/seclists/Passwords/", passw)

check_score = 0

if common_check:
    check_score += 1
if time_check:
    check_score += 1
if default_check:
    check_score += 1
if cracked_check:
    check_score += 1
if general_check:
    check_score += 1

# ----------- Show Results -------------

if check_score != 0:
    cprint(f"\n[+] Your password was found in {check_score} categories!", "red")
else:
    print(f"{MINT_GREEN}\n[+] Your password was not found in any of the checked wordlists!{RESET}")

# Copyright 2026 jbec-dev
