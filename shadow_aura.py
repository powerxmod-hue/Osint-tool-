#!/data/data/com.termux/files/usr/bin/python3
# ==================================================
#    ███████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ██╗    ██╗
#    ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔═══██╗██║    ██║
#    ███████╗███████║███████║██║  ██║██║   ██║██║ █╗ ██║
#    ╚════██║██╔══██║██╔══██║██║  ██║██║   ██║██║███╗██║
#    ███████║██║  ██║██║  ██║██████╔╝╚██████╔╝╚███╔███╔╝
#    ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝ 
#                                                        
#    █████╗ ██╗   ██╗██████╗  █████╗ 
#   ██╔══██╗██║   ██║██╔══██╗██╔══██╗
#   ███████║██║   ██║██████╔╝███████║
#   ██╔══██║██║   ██║██╔══██╗██╔══██║
#   ██║  ██║╚██████╔╝██║  ██║██║  ██║
#   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
# ==================================================
#      💀 SHADOW AURA OSINT - ELITE EDITION v1.0 💀
#               Author: @Babuvikram614
#        "HACK THE PLANET - LEAVE NO TRACE"
# ==================================================

import os
import sys
import time
import json
import requests
import re
import random
from datetime import datetime

# ========== STYLING LIBRARIES ==========
try:
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
except ImportError:
    os.system('pip install colorama')
    from colorama import init, Fore, Back, Style
    init(autoreset=True)

try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.progress import Progress, SpinnerColumn, TextColumn
    from rich import box
    from rich.prompt import Prompt
except ImportError:
    os.system('pip install rich')
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.progress import Progress, SpinnerColumn, TextColumn
    from rich import box
    from rich.prompt import Prompt

console = Console()

# ========== KHATARNAAK BANNERS ==========

# 1. SKULL & CROSSBONES BANNER
SKULL_BANNER = f"""
{Fore.RED}
                                     ▄▄▄▄▄▄▄▄▄▄▄
                                  ▄█████████████████▄
                                ▄███████████████████████▄
                              ▄████████████████████████████▄
                            ▄████████████████████████████████▄
                           ████████████████████████████████████
                         ████████████████████████████████████████
                        ██████████████████████████████████████████
                       ██████████████{Fore.WHITE}▒▒▒▒▒▒▒{Fore.RED}██████████████
                      ████████████{Fore.WHITE}▒▒▒▒▒▒▒▒▒▒▒▒▒{Fore.RED}████████████
                     ████████████{Fore.WHITE}▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒{Fore.RED}███████████
                    ████████████{Fore.WHITE}▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒{Fore.RED}███████████
                   ████████████{Fore.WHITE}▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒{Fore.RED}███████████
                  ████████████{Fore.WHITE}▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒{Fore.RED}███████████
                 ████████████{Fore.WHITE}▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒{Fore.RED}███████████
                ████████████{Fore.WHITE}▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒{Fore.RED}███████████
               ████████████{Fore.WHITE}▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒{Fore.RED}███████████
              ████████████{Fore.WHITE}▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒{Fore.RED}███████████
             ████████████{Fore.WHITE}▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒{Fore.RED}███████████
            ████████████{Fore.WHITE}▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒{Fore.RED}███████████
           ████████████{Fore.WHITE}▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒{Fore.RED}███████████
          ████████████{Fore.WHITE}▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒{Fore.RED}███████████
         ████████████{Fore.WHITE}▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒{Fore.RED}███████████
        ████████████{Fore.WHITE}▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒{Fore.RED}███████████
       ████████████{Fore.WHITE}▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒{Fore.RED}███████████
      ████████████{Fore.WHITE}▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒{Fore.RED}███████████
     ████████████{Fore.WHITE}▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒{Fore.RED}███████████
    ████████████{Fore.WHITE}▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒{Fore.RED}███████████
   ████████████{Fore.WHITE}▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒{Fore.RED}███████████
  ████████████{Fore.WHITE}▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒{Fore.RED}███████████
 ████████████{Fore.WHITE}▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒{Fore.RED}███████████
████████████{Fore.WHITE}▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒{Fore.RED}██████████
███████████{Fore.WHITE}▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒{Fore.RED}█████████
{Fore.RESET}
{Fore.RED}╔════════════════════════════════════════════════════════════════╗
║  {Fore.YELLOW}██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗{Fore.RED}          ║
║  {Fore.YELLOW}██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗{Fore.RED}         ║
║  {Fore.YELLOW}███████║███████║██║     █████╔╝ █████╗  ██████╔╝{Fore.RED}         ║
║  {Fore.YELLOW}██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗{Fore.RED}         ║
║  {Fore.YELLOW}██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║{Fore.RED}         ║
║  {Fore.YELLOW}╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝{Fore.RED}         ║
╚════════════════════════════════════════════════════════════════╝{Fore.RESET}
"""

# 2. MATRIX RAIN BANNER
MATRIX_BANNER = f"""
{Fore.GREEN}01001110 01101111 00100000 01101111 01101110 01100101 00100000 01100011 01100001 01101110 00100000 01101000 01101001 01100100 01100101
00100000 01100110 01110010 01101111 01101101 00100000 01110100 01101000 01100101 00100000 01110011 01101000 01100001 01100100 01101111 01110111
01110011 00101110 00100000 01010111 01100101 00100000 01100001 01110010 01100101 00100000 01100101 01110110 01100101 01110010 01111001 01110111 01101000 01100101 01110010 01100101{Fore.RESET}

{Fore.RED}███████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ██╗    ██╗
██╔════╝██║  ██║██╔══██╗██╔══██╗██╔═══██╗██║    ██║
███████╗███████║███████║██║  ██║██║   ██║██║ █╗ ██║
╚════██║██╔══██║██╔══██║██║  ██║██║   ██║██║███╗██║
███████║██║  ██║██║  ██║██████╔╝╚██████╔╝╚███╔███╔╝
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝{Fore.RESET}

{Fore.GREEN}01100001 01110101 01110010 01100001 00100000 01101001 01110011 00100000 01100101 01110110 01100101 01110010 01111001 01110111 01101000 01100101 01110010 01100101{Fore.RESET}
"""

# 3. HACKER WITH KNIFE BANNER
KNIFE_HACKER = f"""
{Fore.WHITE}                         .---.
{Fore.WHITE}                        /     \\
{Fore.WHITE}                        |  O  |
{Fore.WHITE}                        |  _  |
{Fore.WHITE}                        |  |  |
{Fore.WHITE}                        |  |  |
{Fore.WHITE}                        |  |  |
{Fore.WHITE}                        |  |  |
{Fore.WHITE}                        |  |  |
{Fore.RED}                   _______|  |  |_______
{Fore.RED}                  /  ____  |  |  |   __   \\
{Fore.RED}                 /  /   /  |  |  |   \\ \\  \\
{Fore.RED}                 |  |  /___|  |  |___\\  |  |
{Fore.RED}                 |  |   ____|  |  ____   |  |
{Fore.RED}                 \\  \\  \\   |  |  |   /  /  /
{Fore.RED}                  \\__\\__\\  |__|__|  /__/__/
{Fore.RED}                         \\__________/
{Fore.RED}                              ||||
{Fore.RED}                              ||||
{Fore.RED}                              ||||
{Fore.RED}                         _____||||_____
{Fore.RED}                        |  █████████  |
{Fore.RED}                        |  █████████  |
{Fore.RED}                        |  █████████  |
{Fore.RED}                        |  █████████  |
{Fore.RED}                        |  █████████  |
{Fore.RED}                        |  █████████  |
{Fore.RED}                        |  █████████  |
{Fore.RED}                        |_____________|{Fore.RESET}
{Fore.RED}╔══════════════════════════════════════════╗
║ {Fore.WHITE}SHADOW AURA - CUT THROUGH THE DARK{Fore.RED}   ║
╚══════════════════════════════════════════════╝{Fore.RESET}
"""

# 4. NEON GLITCH EFFECT BANNER
GLITCH_BANNER = f"""
{Fore.MAGENTA}███████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ██╗    ██╗{Fore.CYAN}    █████╗ ██╗   ██╗██████╗  █████╗ 
{Fore.MAGENTA}██╔════╝██║  ██║██╔══██╗██╔══██╗██╔═══██╗██║    ██║{Fore.CYAN}   ██╔══██╗██║   ██║██╔══██╗██╔══██╗
{Fore.MAGENTA}███████╗███████║███████║██║  ██║██║   ██║██║ █╗ ██║{Fore.CYAN}   ███████║██║   ██║██████╔╝███████║
{Fore.MAGENTA}╚════██║██╔══██║██╔══██║██║  ██║██║   ██║██║███╗██║{Fore.CYAN}   ██╔══██║██║   ██║██╔══██╗██╔══██║
{Fore.MAGENTA}███████║██║  ██║██║  ██║██████╔╝╚██████╔╝╚███╔███╔╝{Fore.CYAN}   ██║  ██║╚██████╔╝██║  ██║██║  ██║
{Fore.MAGENTA}╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝ {Fore.CYAN}   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝{Fore.RESET}
{Fore.RED}╔══════════════════════════════════════════════════════════════════════╗
║{Fore.YELLOW}  ░██████╗██╗░░██╗░█████╗░██████╗░░█████╗░░██╗░░░░░░░██╗{Fore.RED}            ║
║{Fore.YELLOW}  ██╔════╝██║░░██║██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║{Fore.RED}            ║
║{Fore.YELLOW}  ╚█████╗░███████║██║░░██║██████╔╝███████║░╚██╗████╗██╔╝{Fore.RED}            ║
║{Fore.YELLOW}  ░╚═══██╗██╔══██║██║░░██║██╔══██╗██╔══██║░░████╔═████║░{Fore.RED}            ║
║{Fore.YELLOW}  ██████╔╝██║░░██║╚█████╔╝██║░░██║██║░░██║░░╚██╔╝░╚██╔╝░{Fore.RED}            ║
║{Fore.YELLOW}  ╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░{Fore.RED}            ║
╚══════════════════════════════════════════════════════════════════════╝{Fore.RESET}
"""

# 5. HOODIE HACKER (existing)
HOODIE_HACKER = f"""
{Fore.GREEN}                         .-.
{Fore.GREEN}                        (o o)
{Fore.GREEN}                        | O |
{Fore.GREEN}                        |   |
{Fore.GREEN}                        '~~~'
{Fore.RED}                ╔═══════════════════════╗
{Fore.RED}                ║  {Fore.CYAN}SHADOW AURA{Fore.RED}         ║
{Fore.RED}                ║  {Fore.YELLOW}██████╗ █████╗ {Fore.RED}    ║
{Fore.RED}                ║  {Fore.YELLOW}██╔══██╗██╔══██╗{Fore.RED}   ║
{Fore.RED}                ║  {Fore.YELLOW}██████╔╝███████║{Fore.RED}   ║
{Fore.RED}                ║  {Fore.YELLOW}██╔═══╝ ██╔══██║{Fore.RED}   ║
{Fore.RED}                ║  {Fore.YELLOW}██║     ██║  ██║{Fore.RED}   ║
{Fore.RED}                ║  {Fore.YELLOW}╚═╝     ╚═╝  ╚═╝{Fore.RED}   ║
{Fore.RED}                ╚═══════════════════════╝
{Fore.RED}                      ╱|\\
{Fore.RED}                     (╯°□°）╯︵ ┻━┻
{Fore.RESET}"""

# 6. ANONYMOUS MASK (existing)
ANON_MASK = f"""
{Fore.CYAN}                 .::!!!!!!!:.
{Fore.CYAN}                .!!!!!:. .!!:
{Fore.CYAN}               ~~~~!!!!!!.
{Fore.CYAN}           .:~XXXXXXXXX~.
{Fore.CYAN}         .:~XXXXXXXXXXXXX~.
{Fore.CYAN}       .:~XXXXXXXXXXXXXXXXX~.
{Fore.CYAN}      :~XXXXXXXXXXXXXXXXXXXXX~.
{Fore.CYAN}     :~XXXXXXXXXXXXXXXXXXXXXXX~:
{Fore.CYAN}    :~XXXXXXX{Fore.RED}###########{Fore.CYAN}XXXXXXX~:
{Fore.CYAN}   :~XXXXXX{Fore.RED}#############{Fore.CYAN}XXXXXXX~:
{Fore.CYAN}  :~XXXXXX{Fore.RED}###############{Fore.CYAN}XXXXXX~:
{Fore.CYAN}  ~XXXXXX{Fore.RED}#################{Fore.CYAN}XXXXXX~
{Fore.CYAN}  ~XXXXX{Fore.RED}###################{Fore.CYAN}XXXXX~
{Fore.CYAN}  ~XXXXX{Fore.RED}###################{Fore.CYAN}XXXXX~
{Fore.CYAN}   ~XXXXX{Fore.RED}#################{Fore.CYAN}XXXXX~
{Fore.CYAN}    ~XXXXX{Fore.RED}###############{Fore.CYAN}XXXXX~
{Fore.CYAN}     ~XXXXXX{Fore.RED}#############{Fore.CYAN}XXXXXX~
{Fore.CYAN}      ~XXXXXXX{Fore.RED}###########{Fore.CYAN}XXXXXXX~
{Fore.CYAN}       ~XXXXXXXXX{Fore.RED}#######{Fore.CYAN}XXXXXXXXX~
{Fore.CYAN}        ~XXXXXXXXXXXXXXXxXXXXXXXXXXXX~
{Fore.CYAN}          ~XXXXXXXXXXXXXXXXXXXXXXXXX~
{Fore.CYAN}            ~"~"~"~"~"~"~"~"~"~"~"~
{Fore.RED}         ╔═══════════════════════════╗
{Fore.RED}         ║  {Fore.WHITE}S H A D O W   A U R A{Fore.RED}    ║
{Fore.RED}         ║  {Fore.YELLOW}WE ARE ANONYMOUS{Fore.RED}        ║
{Fore.RED}         ╚═══════════════════════════╝
{Fore.RESET}"""

# 7. GLASSES HACKER (existing)
GLASSES_HACKER = f"""
{Fore.MAGENTA}            ____________________________
{Fore.MAGENTA}        .-~|                          |~-.
{Fore.MAGENTA}        | |{Fore.WHITE}  [̲̅$̲̅(̲̅ιοο̲̅)̲̅$̲̅]  {Fore.MAGENTA}| |
{Fore.MAGENTA}        '-|__________________________|-'
{Fore.MAGENTA}          /  ●====================●  \\
{Fore.MAGENTA}         |  /                      \\  |
{Fore.MAGENTA}         | |   {Fore.RED}███████╗██╗  ██╗{Fore.MAGENTA}   | |
{Fore.MAGENTA}         | |   {Fore.RED}██╔════╝██║  ██║{Fore.MAGENTA}   | |
{Fore.MAGENTA}         | |   {Fore.RED}███████╗███████║{Fore.MAGENTA}   | |
{Fore.MAGENTA}         | |   {Fore.RED}╚════██║██╔══██║{Fore.MAGENTA}   | |
{Fore.MAGENTA}         | |   {Fore.RED}███████║██║  ██║{Fore.MAGENTA}   | |
{Fore.MAGENTA}         | |   {Fore.RED}╚══════╝╚═╝  ╚═╝{Fore.MAGENTA}   | |
{Fore.MAGENTA}         |  \\______________________/  |
{Fore.MAGENTA}          \\__________________________/
{Fore.MAGENTA}         {Fore.RED}     ╔═══════════════╗
{Fore.MAGENTA}         {Fore.RED}     ║ {Fore.CYAN}SHADOW AURA{Fore.RED}   ║
{Fore.MAGENTA}         {Fore.RED}     ╚═══════════════╝
{Fore.RESET}"""

# 8. TERMINAL HACKER PROFILE (existing)
HACKER_PROFILE = f"""
{Fore.RED}╔{'═'*50}╗
{Fore.RED}║{Fore.WHITE}                      HACKER PROFILE                       {Fore.RED}║
{Fore.RED}╠{'═'*50}╣
{Fore.RED}║{Fore.GREEN}    ╔══╗ ╔══╗ ╔══╗ ╔╗   ╔══╗ ╔══╗ ╔╗ ╔╗ ╔══╗{Fore.RED}             ║
{Fore.RED}║{Fore.GREEN}    ║╔╗║ ║╔╗║ ║╔╗║ ║║   ║╔╗║ ║╔╗║ ║║ ║║ ║╔═╝{Fore.RED}             ║
{Fore.RED}║{Fore.GREEN}    ║╚╝║ ║╚╝║ ║╚╝║ ║║   ║╚╝║ ║╚╝║ ║╚═╝║ ║╚═╗{Fore.RED}             ║
{Fore.RED}║{Fore.GREEN}    ╚═╗║ ╚═╗║ ╚═╗║ ║╚═╗ ║╔╗║ ╚═╗║ ║╔═╗║ ╚═╗║{Fore.RED}             ║
{Fore.RED}║{Fore.GREEN}    ╔═╝║ ╔═╝║ ╔═╝║ ║╔╗║ ║║║║ ╔═╝║ ║║ ║║ ╔═╝║{Fore.RED}             ║
{Fore.RED}║{Fore.GREEN}    ╚══╝ ╚══╝ ╚══╝ ╚╝╚╝ ╚╝╚╝ ╚══╝ ╚╝ ╚╝ ╚══╝{Fore.RED}             ║
{Fore.RED}╠{'═'*50}╣
{Fore.RED}║{Fore.CYAN}  ███████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ██╗    ██╗{Fore.RED}    ║
{Fore.RED}║{Fore.CYAN}  ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔═══██╗██║    ██║{Fore.RED}    ║
{Fore.RED}║{Fore.CYAN}  ███████╗███████║███████║██║  ██║██║   ██║██║ █╗ ██║{Fore.RED}    ║
{Fore.RED}║{Fore.CYAN}  ╚════██║██╔══██║██╔══██║██║  ██║██║   ██║██║███╗██║{Fore.RED}    ║
{Fore.RED}║{Fore.CYAN}  ███████║██║  ██║██║  ██║██████╔╝╚██████╔╝╚███╔███╔╝{Fore.RED}    ║
{Fore.RED}║{Fore.CYAN}  ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝ {Fore.RED}    ║
{Fore.RED}╠{'═'*50}╣
{Fore.RED}║{Fore.YELLOW}  ╔═══════════════════════════════════════════════════╗{Fore.RED}  ║
{Fore.RED}║{Fore.YELLOW}  ║  {Fore.WHITE}██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗{Fore.YELLOW}  ║{Fore.RED}  ║
{Fore.RED}║{Fore.YELLOW}  ║  {Fore.WHITE}██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗{Fore.YELLOW} ║{Fore.RED}  ║
{Fore.RED}║{Fore.YELLOW}  ║  {Fore.WHITE}███████║███████║██║     █████╔╝ █████╗  ██████╔╝{Fore.YELLOW} ║{Fore.RED}  ║
{Fore.RED}║{Fore.YELLOW}  ║  {Fore.WHITE}██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗{Fore.YELLOW} ║{Fore.RED}  ║
{Fore.RED}║{Fore.YELLOW}  ║  {Fore.WHITE}██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║{Fore.YELLOW} ║{Fore.RED}  ║
{Fore.RED}║{Fore.YELLOW}  ║  {Fore.WHITE}╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝{Fore.YELLOW} ║{Fore.RED}  ║
{Fore.RED}║{Fore.YELLOW}  ╚═══════════════════════════════════════════════════╝{Fore.RED}  ║
{Fore.RED}╚{'═'*50}╝{Fore.RESET}"""


# ========== SHADOW AURA APIS - WITH HEADER AUTHENTICATION ==========
class ShadowAuraAPIs:
    """All APIs Pre-Configured with Header Authentication 🔥"""
    
    # 📞 Number API - Header based authentication (like curl command)
    NUM_API = {
        "url": "https://dark-aura-num-info.powerxmod.workers.dev/api?mobile={query}",
        "headers": {"x-api-key": "shadowking"},
        "method": "GET"
    }
    
    # 📧 Email API
    EMAIL_API = {
        "url": "https://shadow-email-info.powerxmod.workers.dev/api?email={query}",
        "headers": {"x-api-key": "shadowaura"},
        "method": "GET"
    }
    
    # 🏦 IFSC API
    IFSC_API = {
        "url": "https://shadow-ifsc-info.powerxmod.workers.dev/api?ifsc={query}",
        "headers": {"x-api-key": "Shadowaura"},
        "method": "GET"
    }
    
    # 🇵🇰 Pakistan API
    PAK_API = {
        "url": "https://shadow-pak-info.powerxmod.workers.dev/api?number={query}",
        "headers": {"x-api-key": "Darkshadow"},
        "method": "GET"
    }
    
    # 🌐 IP API
    IP_API = {
        "url": "https://shadow-ip-info.powerxmod.workers.dev/api?ip={query}",
        "headers": {"x-api-key": "Darkfucker"},
        "method": "GET"
    }
    
    # 🚗 Vehicle API
    VEHICLE_API = {
        "url": "https://shadow-vehicl-info.powerxmod.workers.dev/api?vehicle={query}",
        "headers": {"x-api-key": "Darkaura"},
        "method": "GET"
    }
    
    # 🆔 AADHAR API
    AADHAR_API = {
        "url": "https://shadow-aadhar-info.powerxmod.workers.dev/api?aadhar={query}",
        "headers": {"x-api-key": "Shadowaura"},
        "method": "GET"
    }


# ========== SHADOW AURA MAIN CLASS ==========
class ShadowAura:
    def __init__(self):
        self.name = "SHADOW AURA"
        self.version = "1.0"
        self.author = "@Babuvikram614"
        self.results = {}
        self.scan_count = 0
        self.start_time = datetime.now()
        self.apis = ShadowAuraAPIs()
        
    def clear(self):
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def hacker_banner(self):
        """Main Banner - Random Khatarnaak Banner"""
        self.clear()
        
        # List of all khatarnaak banners
        banners = [
            SKULL_BANNER,
            MATRIX_BANNER,
            KNIFE_HACKER,
            GLITCH_BANNER,
            HOODIE_HACKER,
            ANON_MASK,
            GLASSES_HACKER,
            HACKER_PROFILE
        ]
        
        # Pick a random banner
        banner = random.choice(banners)
        print(banner)
        
        # Print version and info
        print(f"{Fore.RED}╔════════════════════════════════════════════════════════════════╗")
        print(f"{Fore.RED}║{Fore.CYAN}  ⚡ Version: {Fore.WHITE}{self.version} {Fore.RED}|{Fore.CYAN}  Scans: {Fore.WHITE}{self.scan_count} {Fore.RED}|{Fore.CYAN}  Status: {Fore.GREEN}ACTIVE{Fore.RED}   ║")
        print(f"{Fore.RED}║{Fore.CYAN}  💀 Author: {Fore.WHITE}{self.author}{Fore.RED}               |{Fore.CYAN}  APIs: {Fore.GREEN}7/7{Fore.RED}      ║")
        print(f"{Fore.RED}╚════════════════════════════════════════════════════════════════╝{Fore.RESET}")
        
        print(f"{Fore.RED}⚠️  {Fore.YELLOW}WARNING: Only for Educational Purposes! {Fore.RED}⚠️{Fore.RESET}")
        time.sleep(1)
    
    def loading_animation(self, text):
        """Hacker Style Loading Animation"""
        with Progress(
            SpinnerColumn(spinner_name="dots12", style="red"),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task = progress.add_task(f"[bold red]⚡ {text}...", total=None)
            time.sleep(2)
    
    def api_request(self, api_config, query):
        """API request with headers support"""
        try:
            # Format URL with query
            url = api_config["url"].format(query=query)
            headers = api_config.get("headers", {})
            
            # Add random user agent
            ua_list = [
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
            ]
            headers['User-Agent'] = random.choice(ua_list)
            
            response = requests.get(url, headers=headers, timeout=15)
            
            if response.status_code == 200:
                try:
                    return response.json()
                except:
                    return {"data": response.text, "status": "success"}
            else:
                return {"status": "error", "message": f"HTTP {response.status_code}"}
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    def display_results(self, title, data):
        """Display results in table"""
        table = Table(title=f"[bold red]💀 {title} 💀[/bold red]", box=box.HEAVY_EDGE)
        table.add_column("FIELD", style="cyan")
        table.add_column("DATA", style="yellow")
        
        if isinstance(data, dict):
            for key, value in data.items():
                if value and key not in ['status']:
                    # Mask sensitive data
                    if 'mobile' in key.lower() or 'phone' in key.lower() or 'aadhar' in key.lower():
                        if isinstance(value, str) and len(value) > 4:
                            value = value[:2] + "*"*(len(value)-4) + value[-2:]
                    table.add_row(str(key).upper(), str(value))
        else:
            table.add_row("RESULT", str(data))
        
        console.print(Panel(table, border_style="red"))
        self.results[title] = data
        print(f"{Fore.GREEN}[+] DATA EXTRACTED{Fore.RESET}")
    
    # ========== FEATURE FUNCTIONS ==========
    def number_lookup(self):
        console.print(Panel.fit("[bold red]📞 NUMBER OSINT MODULE[/bold red]", border_style="red"))
        number = Prompt.ask("[bold red]💀 Enter Target Phone Number[/bold red]")
        # Clean number
        number = re.sub(r'\D', '', number)
        if len(number) < 10:
            print(f"{Fore.RED}[!] Invalid number! Must be at least 10 digits{Fore.RESET}")
            input(f"\n{Fore.CYAN}[*] Press Enter...{Fore.RESET}")
            return
        
        print(f"{Fore.YELLOW}[!] Fetching data with header authentication...{Fore.RESET}")
        self.loading_animation("Searching database")
        
        result = self.api_request(self.apis.NUM_API, number)
        self.display_results(f"NUMBER: {number}", result)
        self.scan_count += 1
    
    def email_lookup(self):
        console.print(Panel.fit("[bold magenta]📧 EMAIL MODULE[/bold magenta]", border_style="magenta"))
        email = Prompt.ask("[bold red]💀 Enter Target Email[/bold red]")
        print(f"{Fore.YELLOW}[!] Fetching data...{Fore.RESET}")
        self.loading_animation("Searching database")
        
        result = self.api_request(self.apis.EMAIL_API, email)
        self.display_results(f"EMAIL: {email}", result)
        self.scan_count += 1
    
    def ifsc_lookup(self):
        console.print(Panel.fit("[bold green]🏦 IFSC MODULE[/bold green]", border_style="green"))
        ifsc = Prompt.ask("[bold red]💀 Enter IFSC Code[/bold red]").upper()
        if len(ifsc) != 11:
            print(f"{Fore.RED}[!] Invalid IFSC! Must be 11 characters{Fore.RESET}")
            input(f"\n{Fore.CYAN}[*] Press Enter...{Fore.RESET}")
            return
        
        print(f"{Fore.YELLOW}[!] Fetching data...{Fore.RESET}")
        self.loading_animation("Searching database")
        
        result = self.api_request(self.apis.IFSC_API, ifsc)
        self.display_results(f"IFSC: {ifsc}", result)
        self.scan_count += 1
    
    def pakistan_lookup(self):
        console.print(Panel.fit("[bold blue]🇵🇰 PAKISTAN MODULE[/bold blue]", border_style="blue"))
        number = Prompt.ask("[bold red]💀 Enter Pakistan Number (with 03)[/bold red]")
        number = re.sub(r'\D', '', number)
        if len(number) < 10:
            print(f"{Fore.RED}[!] Invalid number!{Fore.RESET}")
            input(f"\n{Fore.CYAN}[*] Press Enter...{Fore.RESET}")
            return
        
        print(f"{Fore.YELLOW}[!] Fetching data...{Fore.RESET}")
        self.loading_animation("Searching database")
        
        result = self.api_request(self.apis.PAK_API, number)
        self.display_results(f"PAKISTAN: {number}", result)
        self.scan_count += 1
    
    def ip_lookup(self):
        console.print(Panel.fit("[bold yellow]🌐 IP MODULE[/bold yellow]", border_style="yellow"))
        ip = Prompt.ask("[bold red]💀 Enter IP Address[/bold red]")
        print(f"{Fore.YELLOW}[!] Fetching data...{Fore.RESET}")
        self.loading_animation("Searching database")
        
        result = self.api_request(self.apis.IP_API, ip)
        self.display_results(f"IP: {ip}", result)
        self.scan_count += 1
    
    def vehicle_lookup(self):
        console.print(Panel.fit("[bold purple]🚗 VEHICLE MODULE[/bold purple]", border_style="purple"))
        vehicle = Prompt.ask("[bold red]💀 Enter Vehicle Number[/bold red]").upper()
        print(f"{Fore.YELLOW}[!] Fetching data...{Fore.RESET}")
        self.loading_animation("Searching database")
        
        result = self.api_request(self.apis.VEHICLE_API, vehicle)
        self.display_results(f"VEHICLE: {vehicle}", result)
        self.scan_count += 1
    
    def aadhar_lookup(self):
        console.print(Panel.fit("[bold red]🆔 AADHAR MODULE[/bold red]", border_style="red"))
        aadhar = Prompt.ask("[bold red]💀 Enter Aadhar Number[/bold red]")
        aadhar = re.sub(r'\D', '', aadhar)
        if len(aadhar) != 12:
            print(f"{Fore.RED}[!] Invalid Aadhar! Must be 12 digits{Fore.RESET}")
            input(f"\n{Fore.CYAN}[*] Press Enter...{Fore.RESET}")
            return
        
        print(f"{Fore.YELLOW}[!] Fetching data...{Fore.RESET}")
        self.loading_animation("Searching database")
        
        result = self.api_request(self.apis.AADHAR_API, aadhar)
        self.display_results(f"AADHAR: {aadhar[-4:]}", result)
        self.scan_count += 1
    
    def save_results(self):
        if not self.results:
            console.print("[bold red]✗ No data to save![/bold red]")
            return
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"shadow_aura_data_{timestamp}.json"
        
        try:
            with open(filename, 'w') as f:
                json.dump({
                    'tool': self.name,
                    'scans': self.scan_count,
                    'results': self.results,
                    'timestamp': str(self.start_time)
                }, f, indent=4)
            
            console.print(f"[bold green]✓ Data saved to {filename}[/bold green]")
        except Exception as e:
            console.print(f"[bold red]✗ Error saving: {e}[/bold red]")
    
    def menu(self):
        while True:
            self.hacker_banner()
            
            menu_table = Table(box=box.DOUBLE_EDGE, border_style="red")
            menu_table.add_column("CODE", style="red", width=8)
            menu_table.add_column("MODULE", style="yellow", width=25)
            
            menu_table.add_row("[1]", "📞 Phone Number")
            menu_table.add_row("[2]", "📧 Email")
            menu_table.add_row("[3]", "🏦 IFSC Code")
            menu_table.add_row("[4]", "🇵🇰 Pakistan Number")
            menu_table.add_row("[5]", "🌐 IP Address")
            menu_table.add_row("[6]", "🚗 Vehicle")
            menu_table.add_row("[7]", "🆔 Aadhar")
            menu_table.add_row("[8]", "💾 Save Data")
            menu_table.add_row("[9]", "📊 Statistics")
            menu_table.add_row("[0]", "🚪 Exit")
            
            console.print(Panel(menu_table, border_style="red"))
            
            choice = Prompt.ask(f"{Fore.RED}SHADOW AURA{Fore.CYAN} ╼{Fore.WHITE} Select", 
                               choices=['1','2','3','4','5','6','7','8','9','0'])
            
            if choice == '1': self.number_lookup()
            elif choice == '2': self.email_lookup()
            elif choice == '3': self.ifsc_lookup()
            elif choice == '4': self.pakistan_lookup()
            elif choice == '5': self.ip_lookup()
            elif choice == '6': self.vehicle_lookup()
            elif choice == '7': self.aadhar_lookup()
            elif choice == '8': self.save_results()
            elif choice == '9':
                console.print(Panel(f"""
[red]Total Scans: {self.scan_count}
Data Files: {len(self.results)}
APIs: 7/7
Started: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}[/red]
""", border_style="red"))
                input(f"\n{Fore.CYAN}[*] Press Enter...{Fore.RESET}")
            elif choice == '0':
                print(f"{Fore.RED}[!] Exiting...{Fore.RESET}")
                sys.exit(0)
            
            if choice in ['1','2','3','4','5','6','7']:
                input(f"\n{Fore.CYAN}[*] Press Enter to continue...{Fore.RESET}")


# ========== MAIN EXECUTION ==========
if __name__ == "__main__":
    try:
        # Check internet
        try:
            requests.get("https://www.google.com", timeout=5)
            print(f"{Fore.GREEN}[✓] Internet Connected{Fore.RESET}")
            time.sleep(1)
        except:
            print(Fore.RED + "[!] No internet!")
            sys.exit(1)
        
        tool = ShadowAura()
        tool.menu()
        
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] Exiting...")
        sys.exit(0)