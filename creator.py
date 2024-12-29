import os
import glob
import random
import time
import requests
from colorama import Fore
from utils.valid import validateToken

invalid = False

# Token input and validation
choice = input("{Fore.RED} Enter Your account Token") # Add your token here
token = validateToken(choice)
import pyfiglet
import os
from colorama import Fore, Style

# Define variables
author = "skidxjija"
# Use the "Ogre" font style in pyfiglet
ravan = pyfiglet.figlet_format("SERVER CREATOR", font="bloody")
made_by = f"[ Made By {author} ]"
centered_made_by = made_by.center(len(ravan))
console_width = 120
centered_ascii_art = "\n".join(line.center(console_width) for line in ravan.split("\n"))
output = centered_ascii_art + f"{centered_made_by}\n"

# Format and display the menu
menu = f"""{Style.BRIGHT}{Fore.RED} {output}\n"""
os.system("clear")
print(menu)
if not invalid:
    headers = {
        'authority': 'discord.com',
        'accept': '*/*',
        'accept-language': 'fr,fr-FR;q=0.9',
        'authorization': token,
        'content-type': 'application/json',
        'origin': 'https://discord.com',
        'referer': 'https://discord.com/channels/@me/1107247318064963624',
        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDQzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI2MzEiLCJvc19hcmNoIjoieDY0IiwiYXBwX2FyY2giOiJpYTMyIiwic3lzdGVtX2xvY2FsZSI6ImZyIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV09XNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIGRpc2NvcmQvMS4wLjkwNDMgQ2hyb21lLzEyMC4wLjYwOTkuMjkxIEVsZWN0cm9uLzI4LjIuMTAgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjI4LjIuMTAiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyODgyMjAsIm5hdGl2ZV9idWlsZF9udW1iZXIiOjQ2OTUyLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsLCJkZXNpZ25faWQiOjB9',
    }

    # Server name input
    name = input(f"{Fore.GREEN}Enter the server name: {Fore.RESET}")

    # Get list of filenames in the Icons folder
    icon_filenames = glob.glob("Icons/*.png")

    # If there are any icons in the folder, select one randomly
    if icon_filenames:
        icon_filename = random.choice(icon_filenames)

        # Open the icon file and read its contents
        with open(icon_filename, "rb") as f:
            icon_data = f.read()

        # Encode the icon data as base64
        import base64
        icon_base64 = base64.b64encode(icon_data).decode()

        # Include the icon data in the request data
        data = f'{{"name":"{name}","icon":"data:image/png;base64,{icon_base64}"}}'
    else:
        data = '{"name":"' + name + '","icon":null}'

    # Ask for the number of servers to create
    while True:
        ask = input(f"{Fore.GREEN}How many servers do you want to create?: {Fore.RESET}")
        if ask.isdigit():
            enablecount = 0  # Initialize the server count
            total_servers = int(ask)
            break
        else:
            print(f"{Fore.RED}Please enter a valid number.{Fore.RESET}")

    # Nitro check for increased server limit
    nitro = input(f"{Fore.GREEN}Do you have Nitro? (y/n): {Fore.RESET}")
    if nitro == "y" or nitro == "yes":
        limit = 200
    else:
        limit = 100

    # Max wait time before each request
    while True:
        Timeinput = input(f"{Fore.GREEN}Enter your max waiting time for the servers to generate (Low term chance & rate limits if high, put 0 for fast): ")
        if Timeinput.isdigit():
            if Timeinput == "0":
                T = 0
                break
            else:
                T = random.uniform(0, float(Timeinput))
                break
        else:
            print(f"{Fore.RED}Please enter a valid number.{Fore.RESET}")

    # Start creating servers
    while enablecount < total_servers:
        if enablecount >= limit:
            print(f"{Fore.MAGENTA} [{Fore.RED}+{Fore.MAGENTA}] {Fore.RESET} You have reached the server limit.")
            break
        else:
            time.sleep(T)  # wait before sending the request
            response = requests.post('https://discord.com/api/v9/guilds', headers=headers, data=data)

            # Check response status code and handle errors
            if response.status_code == 404:
                print(f"{Fore.RED}[ERROR] URL not found. Please check the endpoint.{Fore.RESET}")
            elif response.status_code == 429:
                print(f"{Fore.MAGENTA}[{Fore.RED}+{Fore.MAGENTA}] {Fore.RESET} Rate limited, retrying in 1 second.")
                time.sleep(1)
            elif response.status_code == 401:
                print(f"{Fore.RED}[ERROR] Unauthorized access. Please check your token and try again.{Fore.RESET}")
            elif response.status_code == 201:
                print(f"{Fore.MAGENTA}[{Fore.GREEN}+{Fore.MAGENTA}] {Fore.RESET} Server '{name}' created successfully!")
                enablecount += 1
            else:
                print(f"{Fore.RED}[ERROR] Failed to create server. Status code: {response.status_code} - {response.text}{Fore.RESET}")
                
    print(f"{Fore.MAGENTA}Total servers created: {enablecount}/{total_servers}{Fore.RESET}")

else:
    exit()
