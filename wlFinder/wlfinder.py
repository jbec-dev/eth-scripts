# --------------------------------------
# Wordlist Password Checker by jbec 2026
# --------------------------------------

# -> Uses the most popular wordlists! <-
# -> ! SecLists has to be installed ! <-

import os
import sys
from getpass import getpass

from termcolor import cprint

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

# -------------- Colours ---------------

MINT_GREEN = "\033[38;2;152;251;152m"  # light mint green (RGB)
PASTEL_BLUE = "\033[38;2;176;224;230m"  # powder blue
RESET = "\033[0m"

SECLISTS_ROOT = "/usr/share/seclists"

# ------------- Categories -------------
WORDLIST_CATEGORIES = {
    "common": {
        "directory": "Passwords/Common-Credentials",
        "files": [
            "100k-most-used-passwords-NCSC.txt",
            "xato-net-10-million-passwords.txt",
            "top-20-common-SSH-passwords.txt",
        ],
    },
    "time": {
        "directory": "Passwords",
        "files": ["seasons.txt", "months.txt", "days.txt"],
    },
    "default": {
        "directory": "Passwords/Default-Credentials",
        "files": ["default-passwords.txt", "ssh-betterdefaultpasslist.txt"],
    },
    "cracked": {
        "directory": "Passwords/Cracked-Hashes",
        "files": ["milw0rm-dictionary.txt"],
    },
    "general": {
        "directory": "Passwords",
        "files": ["darkc0de.txt", "openwall.net-all.txt"],
    },
}


# ---------------- Helpers ----------------
def check_category(files, directory, password):
    """Return True if password matches any line in any file in the category."""
    for filename in files:
        wl_file = os.path.join(directory, filename)
        try:
            with open(wl_file, "r", encoding="utf-8", errors="ignore") as handle:
                for line in handle:
                    if password == line.rstrip("\r\n"):
                        return True
        except FileNotFoundError:
            cprint(f"[!] Missing wordlist file: {wl_file}", "yellow")
        except OSError as err:
            cprint(f"[!] Could not read {wl_file}: {err}", "yellow")
    return False


# ---------------- Main ----------------
if not os.path.isdir(SECLISTS_ROOT):
    cprint("Please install SecLists (sudo apt install seclists)!", "red")
    sys.exit(1)

print(f"{MINT_GREEN}[+] SecLists found!{RESET}")

password = getpass(f"{PASTEL_BLUE}[I] Please enter the Password to check: {RESET}")

matched_categories = []
for category_name, category in WORDLIST_CATEGORIES.items():
    category_directory = os.path.join(SECLISTS_ROOT, category["directory"])
    if check_category(category["files"], category_directory, password):
        matched_categories.append(category_name)

# ----------- Show Results -------------
if matched_categories:
    cprint(
        f"\n[+] Your password was found in {len(matched_categories)} categories: "
        + ", ".join(matched_categories),
        "red",
    )
else:
    print(f"{MINT_GREEN}\n[+] Your password was not found in any of the checked wordlists!{RESET}")

# Copyright 2026 jbec-dev
