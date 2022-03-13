#!/usr/bin/python3

import datetime
import links
import requests
import os

from quo import container, echo
from quo.console import Console
from quo.layout import FormattedTextControl, Window
from quo.prompt import Prompt
from quo.text import Text

console = Console()

console.rule()

banner = """
██████╗░██████╗░░█████╗░██████╗░███████╗
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝
██████╔╝██████╔╝██║░░██║██████╦╝█████╗░░
██╔═══╝░██╔══██╗██║░░██║██╔══██╗██╔══╝░░
██║░░░░░██║░░██║╚█████╔╝██████╦╝███████╗
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═════╝░╚══════╝

"""

container(
        Window(
            FormattedTextControl(f"{banner}", style="fg:blue bg:yellow")

            )
        )
echo(f"Created by: Gerrishon Sirere", fg="cyan", bold=True)

def get_time():
    now = datetime.datetime.now()
    return [
            ("bg:green bold", "%s:%s:%s"  % (now.hour, now.minute, now.second)),
            ("bg:yellow fg:black", " Enter Username:")
            ]

session = Prompt(bottom_toolbar=Text('<style fg="red" bg="yellow"> Userprobe v2022.1 </style>'), placeholder=Text('<gray> (please type something)</gray>'), refresh_interval=0.5)

outputFolder = 'output'
echo('', nl=True)

username = session.prompt(get_time)

echo(f"Finding Accounts", italic=True, reverse=True)
class ReCon:
    def __init__(
            self,
            site_name, 
            social_url, 
            username, 
            output
            ):
        self.site_name = site_name
        self.social_url = social_url
        self.name = username
        self.output = output
    def find_account(self):
        try:
            response = requests.get(self.social_url.format(self.name), timeout=5) 
            if response.status_code == 200:
                echo(f"[+] Found {self.site_name}, {self.social_url.format(self.name)}", fg="cyan")
                
                ifexist = os.path.exists(self.output)
                if ifexist == False:
                    os.mkdir(self.output)
                    file = open(f'{self.output}/{self.name}.txt','a')
                    file.write(f'{self.social_url.format(self.name)}\n')
                elif ifexist == True:
                    file = open(f'{self.output}/{self.name}.txt','a')
                    file.write(f'{self.social_url.format(self.name)}\n')
                    
                else:
                    echo(f"Something Went Wrong", fg="red")

            else:
                echo(f"[x] Not found on: ", nl=False, bg="red")
                echo(f"{ self.site_name}", fg="green")
        except requests.exceptions.ReadTimeout:
            echo(f"[x] Not found on: {self.site_name} :Request timed out", bg="red")
for i in links.links:
    ReCon(i, links.links[i], username, outputFolder).find_account()

echo(f'Thanks for using probe')
