#!/data/data/com.termux/files/usr/bin/python3
# ==================================================
#          ███████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ██╗    ██╗
#          ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔═══██╗██║    ██║
#          ███████╗███████║███████║██║  ██║██║   ██║██║ █╗ ██║
#          ╚════██║██╔══██║██╔══██║██║  ██║██║   ██║██║███╗██║
#          ███████║██║  ██║██║  ██║██████╔╝╚██████╔╝╚███╔███╔╝
#          ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝ 
#                                                              
#          █████╗ ██╗   ██╗██████╗  █████╗ 
#         ██╔══██╗██║   ██║██╔══██╗██╔══██╗
#         ███████║██║   ██║██████╔╝███████║
#         ██╔══██║██║   ██║██╔══██╗██╔══██║
#         ██║  ██║╚██████╔╝██║  ██║██║  ██║
#         ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
# ==================================================
#         SHADOW AURA OSINT - ELITE EDITION v1.0
#                  Author: @Babuvikram614
#               All APIs Pre-Configured ✓
# ==================================================

import os
import sys
import time
import json
import requests
from datetime import datetime
import platform
import random

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

# ========== SHADOW AURA APIS ==========
class ShadowAuraAPIs:
    """All APIs Pre-Configured - Ready to Use! 🔥"""
    
    # 📞 Number API
    NUM_API = "https://shado-aura-api.babuvikram614.workers.dev/?number={query}&key=Shadowaura"
    
    # 📧 Email API
    EMAIL_API = "https://abbas-apis.vercel.app/api/email?mail={query}"
    
    # 🏦 IFSC API
    IFSC_API = "http://shadowaura-ifsc-info-api.babuvikram614.workers.dev/?code={query}&key=Shadowaura"
    
    # 🇵🇰 Pakistan API
    PAK_API = "https://darkshadow-pak-info.babuvikram614.workers.dev/?number={query}&key=Darkshadow"
    
    # 🌐 IP API
    IP_API = "http://darkfucker-shadow-aura-ip.babuvikram614.workers.dev/?ip={query}&key=Darkfucker"
    
    # 🚗 Vehicle API
    VEHICLE_API = "https://shadow-aura-vehicle-info.babuvikram614.workers.dev/?vehicle={query}&key=Darkaura"
    
    # 🆔 AADHAR API
    AADHAR_API = "https://shadow-aura-aadha-info.babuvikram614.workers.dev/?match={query}&key=Shadowaura"


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
        """Main Banner - Hacker Style"""
        self.clear()
        banner = f"""
{Fore.RED}╔══════════════════════════════════════════════════════════════════════════════╗
{Fore.RED}║  {Fore.WHITE}███████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ██╗    ██╗{Fore.RED}                   ║
{Fore.RED}║  {Fore.WHITE}██╔════╝██║  ██║██╔══██╗██╔══██╗██╔═══██╗██║    ██║{Fore.RED}                   ║
{Fore.RED}║  {Fore.WHITE}███████╗███████║███████║██║  ██║██║   ██║██║ █╗ ██║{Fore.RED}                   ║
{Fore.RED}║  {Fore.WHITE}╚════██║██╔══██║██╔══██║██║  ██║██║   ██║██║███╗██║{Fore.RED}                   ║
{Fore.RED}║  {Fore.WHITE}███████║██║  ██║██║  ██║██████╔╝╚██████╔╝╚███╔███╔╝{Fore.RED}                   ║
{Fore.RED}║  {Fore.WHITE}╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝ {Fore.RED}                   ║
{Fore.RED}╠══════════════════════════════════════════════════════════════════════════════╣
{Fore.RED}║  {Fore.CYAN}► OSINT ELITE TOOL {Fore.WHITE}|{Fore.CYAN} Version: {Fore.WHITE}{self.version} {Fore.WHITE}|{Fore.CYAN} Author: {Fore.WHITE}{self.author} {Fore.RED}                  ║
{Fore.RED}║  {Fore.CYAN}► Scans: {Fore.WHITE}{self.scan_count} {Fore.WHITE}|{Fore.CYAN} Started: {Fore.WHITE}{self.start_time.strftime('%H:%M:%S')} {Fore.RED}                           ║
{Fore.RED}║  {Fore.CYAN}► APIs: {Fore.WHITE}7/7 Configured {Fore.GREEN}[✓]{Fore.RED}                                        ║
{Fore.RED}╚══════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
        """
        print(banner)
        time.sleep(0.5)
    
    def loading_animation(self, text):
        """Loading Animation"""
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task = progress.add_task(f"[cyan]{text}...", total=None)
            time.sleep(1.5)
    
    def api_request(self, url):
        """API request with error handling"""
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 11; SM-G998B)'}
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
        """Display results in rich table"""
        table = Table(title=f"[bold red]{title}[/bold red]", box=box.DOUBLE_EDGE, border_style="red")
        table.add_column("Field", style="cyan", no_wrap=True)
        table.add_column("Value", style="green")
        
        if isinstance(data, dict):
            for key, value in data.items():
                if value and key not in ['status']:
                    table.add_row(str(key), str(value))
        else:
            table.add_row("Data", str(data))
        
        console.print(table)
        self.results[title] = data
    
    # ========== FEATURE 1: NUMBER LOOKUP ==========
    def number_lookup(self):
        console.print(Panel.fit("[bold cyan]📞 NUMBER OSINT MODULE[/bold cyan]", border_style="cyan"))
        number = Prompt.ask("[bold yellow]Enter Phone Number[/bold yellow]")
        
        self.loading_animation(f"Querying Shadow Aura Database for {number}")
        url = self.apis.NUM_API.format(query=number)
        result = self.api_request(url)
        
        self.display_results(f"NUMBER INFO: {number}", result)
        self.scan_count += 1
    
    # ========== FEATURE 2: EMAIL LOOKUP ==========
    def email_lookup(self):
        console.print(Panel.fit("[bold magenta]📧 EMAIL OSINT MODULE[/bold magenta]", border_style="magenta"))
        email = Prompt.ask("[bold yellow]Enter Email Address[/bold yellow]")
        
        self.loading_animation(f"Scanning Email Databases for {email}")
        url = self.apis.EMAIL_API.format(query=email)
        result = self.api_request(url)
        
        self.display_results(f"EMAIL INFO: {email}", result)
        self.scan_count += 1
    
    # ========== FEATURE 3: IFSC LOOKUP ==========
    def ifsc_lookup(self):
        console.print(Panel.fit("[bold green]🏦 IFSC BANK MODULE[/bold green]", border_style="green"))
        ifsc = Prompt.ask("[bold yellow]Enter IFSC Code[/bold yellow]").upper()
        
        self.loading_animation(f"Fetching Bank Details for {ifsc}")
        url = self.apis.IFSC_API.format(query=ifsc)
        result = self.api_request(url)
        
        self.display_results(f"BANK INFO: {ifsc}", result)
        self.scan_count += 1
    
    # ========== FEATURE 4: PAKISTAN NUMBER LOOKUP ==========
    def pakistan_lookup(self):
        console.print(Panel.fit("[bold blue]🇵🇰 PAKISTAN NUMBER MODULE[/bold blue]", border_style="blue"))
        number = Prompt.ask("[bold yellow]Enter Pakistan Number (with 03)[/bold yellow]")
        
        self.loading_animation(f"Accessing Pakistan Telecom Database")
        url = self.apis.PAK_API.format(query=number)
        result = self.api_request(url)
        
        self.display_results(f"PAKISTAN NUMBER: {number}", result)
        self.scan_count += 1
    
    # ========== FEATURE 5: IP LOOKUP ==========
    def ip_lookup(self):
        console.print(Panel.fit("[bold yellow]🌐 IP GEOLOCATION MODULE[/bold yellow]", border_style="yellow"))
        ip = Prompt.ask("[bold yellow]Enter IP Address[/bold yellow]")
        
        self.loading_animation(f"Tracking IP Location - {ip}")
        url = self.apis.IP_API.format(query=ip)
        result = self.api_request(url)
        
        self.display_results(f"IP INFO: {ip}", result)
        self.scan_count += 1
    
    # ========== FEATURE 6: VEHICLE LOOKUP ==========
    def vehicle_lookup(self):
        console.print(Panel.fit("[bold purple]🚗 VEHICLE REGISTRATION MODULE[/bold purple]", border_style="purple"))
        vehicle = Prompt.ask("[bold yellow]Enter Vehicle Number[/bold yellow]")
        
        self.loading_animation(f"Checking RTO Database for {vehicle}")
        url = self.apis.VEHICLE_API.format(query=vehicle)
        result = self.api_request(url)
        
        self.display_results(f"VEHICLE INFO: {vehicle}", result)
        self.scan_count += 1
    
    # ========== FEATURE 7: AADHAR LOOKUP ==========
    def aadhar_lookup(self):
        console.print(Panel.fit("[bold red]🆔 AADHAR VERIFICATION MODULE[/bold red]", border_style="red"))
        aadhar = Prompt.ask("[bold yellow]Enter Aadhar Number[/bold yellow]")
        
        self.loading_animation(f"Verifying Aadhar in UIDAI Database")
        url = self.apis.AADHAR_API.format(query=aadhar)
        result = self.api_request(url)
        
        self.display_results(f"AADHAR INFO: {aadhar[-4:]}", result)
        self.scan_count += 1
    
    # ========== SAVE RESULTS ==========
    def save_results(self):
        if not self.results:
            console.print("[bold red]✗ No results to save![/bold red]")
            return
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"shadow_aura_{timestamp}.json"
        
        try:
            with open(filename, 'w') as f:
                json.dump({
                    'tool': self.name,
                    'scans': self.scan_count,
                    'results': self.results
                }, f, indent=4)
            
            console.print(f"[bold green]✓ Results saved to {filename}[/bold green]")
        except Exception as e:
            console.print(f"[bold red]✗ Error saving: {e}[/bold red]")
    
    # ========== MAIN MENU ==========
    def menu(self):
        while True:
            self.hacker_banner()
            
            menu_table = Table(box=box.ROUNDED, border_style="red", show_header=True, header_style="bold red")
            menu_table.add_column("Option", style="cyan", width=8)
            menu_table.add_column("Module", style="yellow", width=25)
            menu_table.add_column("Status", style="green", width=15)
            
            menu_table.add_row("[1]", "📞 Number Lookup", "READY ✓")
            menu_table.add_row("[2]", "📧 Email Lookup", "READY ✓")
            menu_table.add_row("[3]", "🏦 IFSC Code", "READY ✓")
            menu_table.add_row("[4]", "🇵🇰 Pakistan Number", "READY ✓")
            menu_table.add_row("[5]", "🌐 IP Geolocation", "READY ✓")
            menu_table.add_row("[6]", "🚗 Vehicle Info", "READY ✓")
            menu_table.add_row("[7]", "🆔 Aadhar Lookup", "READY ✓")
            menu_table.add_row("[8]", "💾 Save Results", f"({len(self.results)} items)")
            menu_table.add_row("[9]", "📊 Show Stats", "-")
            menu_table.add_row("[0]", "🚪 Exit", "-")
            
            console.print(menu_table)
            
            choice = Prompt.ask(f"[bold red]SHADOW AURA[/bold red] [cyan]╼[/cyan] [bold white]Select option[/bold white]", 
                               choices=['1','2','3','4','5','6','7','8','9','0'])
            
            if choice == '1':
                self.number_lookup()
            elif choice == '2':
                self.email_lookup()
            elif choice == '3':
                self.ifsc_lookup()
            elif choice == '4':
                self.pakistan_lookup()
            elif choice == '5':
                self.ip_lookup()
            elif choice == '6':
                self.vehicle_lookup()
            elif choice == '7':
                self.aadhar_lookup()
            elif choice == '8':
                self.save_results()
            elif choice == '9':
                stats_table = Table(title="SHADOW AURA STATISTICS", box=box.DOUBLE_EDGE)
                stats_table.add_column("Metric", style="cyan")
                stats_table.add_column("Value", style="green")
                stats_table.add_row("Total Scans", str(self.scan_count))
                stats_table.add_row("Results Saved", str(len(self.results)))
                stats_table.add_row("APIs Configured", "7/7")
                stats_table.add_row("Session Started", self.start_time.strftime('%Y-%m-%d %H:%M:%S'))
                console.print(stats_table)
                input("\n[bold cyan]Press Enter...[/bold cyan]")
            elif choice == '0':
                console.print("[bold red]Shutting Down Shadow Aura...[/bold red]")
                time.sleep(1)
                sys.exit(0)
            
            if choice in ['1','2','3','4','5','6','7']:
                input("\n[bold cyan]Press Enter to continue...[/bold cyan]")


# ========== MAIN EXECUTION ==========
if __name__ == "__main__":
    try:
        # Check internet
        try:
            requests.get("https://www.google.com", timeout=5)
        except:
            print(Fore.RED + "[!] No internet connection!")
            sys.exit(1)
        
        tool = ShadowAura()
        tool.menu()
        
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] Exiting...")
        sys.exit(0)