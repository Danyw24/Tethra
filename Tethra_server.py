#Tethra serve
#Developed by danyw24
# 0.1v
# Server

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

#importing modules



from email import message
import threading
import socket
import time
from os import system

from server import broadcast
host = 'localhost'
port = 8080
skserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
skserver.bind((host, port))
skserver.listen(5)
print(f"{success} Server listening on: {host}:{port}")

connections = []
usernames = []

def recive_connections():
    while True:
        connection, address = skserver.accept()
      
        connection.send("@username".encode("utf-8"))
        username = connection.recv(1024).decode("utf-8")
        
        usernames.append(username)
        connections.append(connection)

        message = f"{success} New connetion : {username}".encode("utf-8")
        broadcast(message, connection)
        print(f"{info} Address: {address}, Time: D{time.localtime().tm_mday} {time.localtime().tm_hour}h {time.localtime().tm_min}min {time.localtime().tm_sec}sec")

        thread_rm = threading.Thread(target=recive_messages, args=(connection,))
        thread_rm.start()
   

def Broadcast(message, client):
    for connection in connections:
        if connection != client:
            connection.send(message)


def recive_messages(connection):
    while True:
        try: 
           message = connection.recv(1024)
           Broadcast(message, connection)
        except:
            index = connections.index(connection)
            username = usernames[index]
            connections.remove(connection)
            usernames.remove(username)
            Broadcast(f"{info} {connection} has left...".encode("utf-8"), connection)
            connection.close()
            break



recive_connections()




