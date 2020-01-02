import datetime
import os
import sys
import names
import random
import string
import time
from threading import Thread
import requests
from proxymanager import ProxyManager


bodegawrite =open(os.path.join(sys.path[0], "BodegaAccounts.txt"),"a")
fogwrite =open(os.path.join(sys.path[0], "FOGAccounts.txt"),"a")
cnptswrite=open(os.path.join(sys.path[0], "ConceptsAccounts.txt"),"a")
print('''
    _____ _                 _  __                                           _      _____                           _             
    / ____| |               (_)/ _|           /\                            | |    / ____|                         | |            
    | (___ | |__   ___  _ __  _| |_ _   _     /  \   ___ ___ ___  _   _ _ __ | |_  | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
    \___ \| '_ \ / _ \| '_ \| |  _| | | |   / /\ \ / __/ __/ _ \| | | | '_ \| __| | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
    ____) | | | | (_) | |_) | | | | |_| |  / ____ \ (_| (_| (_) | |_| | | | | |_  | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
    |_____/|_| |_|\___/| .__/|_|_|  \__, | /_/    \_\___\___\___/ \__,_|_| |_|\__|  \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
    ______     __     | |   _       __/ | _  _    ___   ___   ___ ___                                                             
    |  _ \ \   / /     /\|  | |     |___/_| || |_ / _ \ / _ \ / _ \__ \                                                            
    | |_) \ \_/ /     /  \  | | _____  _|_  __  _| | | | | | | | | | ) |                                                           
    |  _ < \   /     / /\ \ | |/ _ \ \/ /_| || |_| | | | | | | | | |/ /                                                            
    | |_) | | |     / ____ \| |  __/>  <|_  __  _| |_| | |_| | |_| / /_                                                            
    |____/  |_|    /_/____\_\_|\___/_/\_\ |_||_|  \___/ \___/ \___/____|                    
                                    
    ''')

accounts_number =int(input("How many accounts would like to create: "))
site = input('''What site would you like create accounts for
        1- Bodega
        2- Fear of God
        3- CNCPTS

        ''')
catchall= input("Please input your catchall E.G aamenace.com: ")
password= input("Please input what password you would like to use: ")
def main(accounts_number):
        

        

    with open(os.path.join(sys.path[0], "ShopifyAccounts.txt"), "r+") as accounts:
        x = str(datetime.datetime.now())
        accounts.write(x+"\n")
        if FileNotFoundError in accounts:
            print ("FATAL ERROR: NO ACCOUNTS FILE FOUND, TELL ALEX TO FIX THIS")



    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
        }


    def Bodega():
        
        
        
        
        import random
        with open(os.path.join(sys.path[0], "proxies.txt"), "r") as f:
            lines = f.read().splitlines()
            proxies= random.choice(lines)
            proxySplit= proxies.split(":")
            proxyDict = {
                    "http": "http://" + proxySplit[2] + ":" + proxySplit[3] + "@" + proxySplit[0] + ":" + proxySplit[1] + "/",
                    "https": "https://" + proxySplit[2] + ":" + proxySplit[3] + "@" + proxySplit[0] + ":" + proxySplit[1] + "/"
                }
        randomname = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(10)])
        email = randomname+"@"+catchall
        payload = {
        "form_type": "create_customer",
        "utf8": "✓",
        "customer[first_name]": "John",
        "customer[last_name]": "Doe",
        "customer[email]": email,
        "customer[password]": password
        }
        bodegaacc= requests.post("https://bdgastore.com/account", data=payload, headers=headers, proxies=proxyDict)
        if bodegaacc.status_code == 200:
            print("Bodgea Account Creation successful")
        bodegawrite.write(email+":"+password+"\n")
        with open(os.path.join(sys.path[0], "proxies.txt"), "w") as f:
            for line in lines:
                if line.strip("\n") != proxies:
                    f.write(line+"\n")             
    def FOG():
        import random
        
        with open(os.path.join(sys.path[0], "proxies.txt"), "r") as f:
            lines = f.read().splitlines()
            proxies= random.choice(lines)
            proxySplit= proxies.split(":")
            proxyDict = {
                    "http": "http://" + proxySplit[2] + ":" + proxySplit[3] + "@" + proxySplit[0] + ":" + proxySplit[1] + "/",
                    "https": "https://" + proxySplit[2] + ":" + proxySplit[3] + "@" + proxySplit[0] + ":" + proxySplit[1] + "/"
                }
        randomname = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(10)])
        email = randomname+"@"+catchall
        payload = {
        "form_type": "create_customer",
        "utf8": "✓",
        "customer[first_name]": "John",
        "customer[last_name]": "Doe",
        "customer[email]": email,
        "customer[password]": password
    }
        bodegaacc= requests.post("https://fearofgod.com/account", data=payload, headers=headers, proxies=proxyDict)
        if bodegaacc.status_code == 200:
            print("Fear of God Account Creation successful")
        fogwrite.write(email+":"+password+"\n")
            
            
        
        
        with open(os.path.join(sys.path[0], "proxies.txt"), "w") as f:
            for line in lines:
                if line.strip("\n") != proxies:
                    f.write(line+"\n")             

    def Concepts():
        
        import random
            
        with open(os.path.join(sys.path[0], "proxies.txt"), "r") as f:
            lines = f.read().splitlines()
            proxies= random.choice(lines)
            proxySplit= proxies.split(":")
            proxyDict = {
                    "http": "http://" + proxySplit[2] + ":" + proxySplit[3] + "@" + proxySplit[0] + ":" + proxySplit[1] + "/",
                    "https": "https://" + proxySplit[2] + ":" + proxySplit[3] + "@" + proxySplit[0] + ":" + proxySplit[1] + "/"
                }
        randomname = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(10)])
        email = randomname+"@"+catchall
        payload = {
        "form_type": "create_customer",
        "utf8": "✓",
        "customer[first_name]": "John",
        "customer[last_name]": "Doe",
        "customer[email]": email,
        "customer[password]": password
    }
        bodegaacc= requests.post("https://cncpts.com/account", data=payload, headers=headers, proxies=proxyDict, allow_redirects=True)
        conacc = bodegaacc.url
        if conacc.status_code == 200:
            print("Concepts Account Creation successful")
        fogwrite.write(email+":"+password+"\n")
            
            
    
    
        with open(os.path.join(sys.path[0], "proxies.txt"), "w") as f:
            for line in lines:
                if line.strip("\n") != proxies:
                    f.write(line+"\n")             


    if site== "1":
        Bodega()
    if site=="2":
        FOG()
    if site=="3":
        Concepts()
    
for i in range(accounts_number):
    t = Thread(target=main, args=(i,))
    t.start()
