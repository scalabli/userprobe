#!/usr/bin/python

import links
from quo import prompt, echo
import requests
import os

echo(f"Created by: Gerrishon Sirere", fg="cyan", bold=True)




outputFolder = 'output'
print('\n')

username = prompt(echo(f"Enter username", fg="black", bg="vyellow"),type=str)

echo(f"Finding Accounts", italic=True, reverse=True)
class ReCon:
    def __init__(self,site_name, social_url, username, output):
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
                echo(f"[x] Not found: { self.site_name}", bg="red")
        except requests.exceptions.ReadTimeout:
            echo(f"[x] Not found: {self.site_name} :Request timed out", bg="red")
for i in links.links:
    ReCon(i, links.links[i], username, outputFolder).find_account()

print(f'Thanks for using probe')
