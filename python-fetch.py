#!/usr/bin/env python3
#Created by PepeBigotes
#===========================[INDEX]=============================#
# (Navigate using the search feature of your code/text editor)  #
#                                                               #
#1. Imports (aka Dependencies)
#2. Color Class
#3. Username, Hostname
#4. Welcome, Underline, Suffix Config
# 4.1. Welcome
# 4.2. Underline
# 4.3. Suffix
#5. Time, Date , Battery, IPs
#6. Disk Class



#1. Imports (aka Dependencies)
import colored #pip install colored
import requests #pip install requests
import time
import datetime
import string
import socket
import os
import psutil
import shutil

rows, columns = os.popen('stty size', 'r').read().split()

#2. Color Class
# See https://pypi.org/project/colored/ for more info
class color:
   c0 = colored.fg('#FFFFFF')
   c1 = colored.fg('#A0FFA0')
   c2 = colored.fg('#A9DFA9')
   
   bold = colored.attr("bold")
   reset = colored.attr("reset")


#3. Username, Hostname
username = os.getlogin()
hostname = socket.gethostname()   

#4. Welcome, Underline, Suffix Config
# 4.1. Welcome
welcome_p = [ username, "@", hostname ]
welcome_sum = "".join(map(str, welcome_p))

welcome = ""
welcome += color.bold + color.c1 + welcome_p[0] + color.reset
welcome += color.bold + color.c0 + welcome_p[1] + color.reset
welcome += color.bold + color.c2 + welcome_p[2] + color.reset

# 4.2. Underline
underline_symbol = "="
underline = underline_symbol * len(welcome_sum)
# 4.3. Suffix
default_suffix = ": "


#5. Time, Date , Battery, IPs
#Hour/Minute
time_hm = time.strftime("%H:%M")

datetimenow = datetime.datetime.now()
#Day/Month/Year
date_dmy = datetimenow.strftime("%d/%m/%y")

uptime_secs = time.time() - psutil.boot_time()
# Formated uptime: day, hh:mm:ss
uptime = str(datetime.timedelta(seconds=uptime_secs))

battery = psutil.sensors_battery()
if battery != None:
   plugged = battery.power_plugged
   percent = str(int(battery.percent))
   plugged = " (Charging...)" if plugged else ""

# IPs
local_ip = socket.gethostbyname(hostname)
public_ip = requests.get('https://ident.me/').content.decode('utf8')

#6. Disk Class
class disk:
   total, used, free = shutil.disk_usage("/")
   total_gib = total // (2**30)
   used_gib = used // (2**30)
   free_gib = free // (2**30)
   used_percert =round( (used_gib / total_gib) * 100)
   free_percert = round( (free_gib / total_gib) * 100)


def info(text = "", info = "" , suffix = default_suffix):
   if text == "" or info == "":
      suffix = ""
   
   print(text + suffix + info)

info(welcome)
info(underline)

#info("Host", hostname)
info("Uptime" , uptime)
info("Time" , time_hm)
info("Date" , date_dmy)
#info("Battery", percent + '%' + plugged)
info("Disk" ,  str(disk.used_gib) + "/" + str(disk.total_gib) + " GiB (" + str(disk.used_percert) + "%)")
info("Local IP" , local_ip)
#info("Public IP" , public_ip)
info()