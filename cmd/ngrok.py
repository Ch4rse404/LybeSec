import os

print("""
[ 1 ] TCP 

[ 2 ] HTTP
""")

opc = input('digite sua opcao:')

if opc == '1':
    ngrokt = input('porta:')
    os.system(f'./ngrok tcp {ngrokt}')
elif opc == '2':
    ngrok = input('porta:')
    os.system(f'./ngrok http {ngrokh}')
else:
    print('[+] ERRO')