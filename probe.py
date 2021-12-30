#!/usr/bin/python

import links
import quo
import requests
import os

banner = """
██████╗░██████╗░░█████╗░██████╗░███████╗
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝
██████╔╝██████╔╝██║░░██║██████╦╝█████╗░░
██╔═══╝░██╔══██╗██║░░██║██╔══██╗██╔══╝░░
██║░░░░░██║░░██║╚█████╔╝██████╦╝███████╗
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═════╝░╚══════╝

"""

quo.echo(f"{banner}", fg="vblue")
quo.echo(f"Created by: Gerrishon Sirere", fg="cyan", bold=True)


session = quo.Prompt(bottom_toolbar=quo.text.HTML('<style fg="red" bg="yellow"> Probe v2021.2 </style>'), placeholder=quo.text.HTML('<style fg ="gray"> (please type something)</style>'))

outputFolder = 'output'
quo.echo('', nl=True)

username = session.prompt("Enter username: ")

quo.echo(f"Finding Accounts", italic=True, reverse=True)
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
                quo.echo(f"[+] Found {self.site_name}, {self.social_url.format(self.name)}", fg="cyan")
                
                ifexist = os.path.exists(self.output)
                if ifexist == False:
                    os.mkdir(self.output)
                    file = open(f'{self.output}/{self.name}.txt','a')
                    file.write(f'{self.social_url.format(self.name)}\n')
                elif ifexist == True:
                    file = open(f'{self.output}/{self.name}.txt','a')
                    file.write(f'{self.social_url.format(self.name)}\n')
                    
                else:
                    quo.echo(f"Something Went Wrong", fg="red")

            else:
                quo.echo(f"[x] Not found: { self.site_name}", bg="red")
        except requests.exceptions.ReadTimeout:
            quo.echo(f"[x] Not found: {self.site_name} :Request timed out", bg="red")
for i in links.links:
    ReCon(i, links.links[i], username, outputFolder).find_account()

quo.echo(f'Thanks for using probe')
