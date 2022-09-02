# TETHRA
# Developed by danyw24 
# 0.1v
# Encrypted chat system 


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

# Regular Snippets
ask  =     f"{green}[{white}?{green}] {yellow}"
success = f"{yellow}[{white}√{yellow}] {green}"
error  =    f"{blue}[{white}!{blue}] {red}"
info  =   f"{yellow}[{white}+{yellow}] {cyan}"
info2  =   f"{green}[{white}•{green}] {purple}"



#import modules

import threading
import os
import socket
from time import sleep

#Intro
os.system("@echo off && cls && Color 02")
def printIntro():     
    interface_img_1 = f"""



               ...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO                          ______     __  __              
       ::::::;       ;          OOOOO                        /_  __/__  / /_/ /_  _________ _
       ;:::::;       ;         OOOOOOOO                       / / / _ \/ __/ __ \/ ___/ __ `/
      ,;::::::;     ;'         / OOOOOOO                     / / /  __/ /_/ / / / /  / /_/ / 
    ;:::::::::`. ,,,;.        /  / DOOOOOO                  /_/  \___/\__/_/ /_/_/   \__,_/ 
  .';:::::::::::::::::;,     /  /     DOOOO                                    
 ,::::::;::::::;;;;::::;,   /  /        DOOO                     Developed by Danyw24
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O
  `:::::`::::::::;' /  / `:#
   ::::::`:::::;'  /  /   `#


            """ 
    print(interface_img_1)
    sleep(3)
    os.system("cls")
printIntro()
username = input(f"{ask} Enter your username (All users can will see your username): ")

# Creating user
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 8080))

def recive_messages():
  while True:
    try:
      message = client.recv(1024).decode("utf-8")

      if message == "@username":
        client.send(username.encode("utf-8")) #Encoding messages with utf8
      else:
        print(message)
    except:
      print(f"{error} An error ocurred ")
      client.close()
      break
      

def send_messages():
  while True:
    message = f"{username}: {input('')}"
    client.send(message.encode("utf-8"))


thread_rm = threading.Thread(target=recive_messages)
thread_rm.start()

thread_sd = threading.Thread(target=send_messages)
thread_sd.start()
