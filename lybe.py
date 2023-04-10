import sys, time
from sys import argv, executable

from ini import banner

def restart():
    
    lybe = input("\033[92m$Lybe\033[0m@\033[92mroot/\033[0m~")
    
    if lybe == 'fet tekshell':
        from TekShell import tekshell
        restart()
    elif lybe == 'fet neofetch':
        from ini import neofetch
        restart()
    elif lybe == 'fet exit':
        os.system('exit')
    elif lybe == '--help':
        from ini import hp
        restart()
    elif lybe == 'fet update':
        os.system('apt upgrade')
        restart()
    elif lybe == 'fet version':
        print("version 1.0")
        restart()
    elif lybe == 'fet dev':
        print("desenvolvido pelo ch4rse")
        restart()
    elif lybe == 'fet criadores':
        from devs import criadores
        restart()
    elif lybe == 'fet sqlmap':
        from derb import sqlmap
    elif lybe == 'fet lybedos':
        from derb import lybedos
    elif lybe == 'fet netcat':
        from cmd import netcat
    elif lybe == 'fet ngrok':
        from cmd import ngrok
    elif lybe == 'fet calculadora':
        from derb import calculadora
    elif lybe == 'fet portscan':
        from derb import portscan
    elif lybe == 'fet nmap':
        from cmd import nmap
        restart()
    elif lybe == 'fet geoip':
        from derb import geoip
    elif lybe == 'fet cnpj':
        from cons import cnpj
        restart()
    elif lybe == 'fet cep':
        from cons import cep
        restart()
    elif lybe == 'fet phishing':
        from phi import phishing
        
restart()