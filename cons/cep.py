az = '\033[1;94m'
cia = '\033[1;36m'
ba = '\033[1;37m'
ro = '\033[1;35m'
v = '\033[1;31m'

import requests, os, re, time

print("""
 ::::::::  :::::::::: :::::::::  
:+:    :+: :+:        :+:    :+: 
+:+        +:+        +:+    +:+ 
+#+        +#++:++#   +#++:++#+  
+#+        +#+        +#+        
#+#    #+# #+#        #+#        
 ########  ########## ###        """)
 
def Cep():
    os.system('figlet CEPconsu')
    cep = input(f'{cia}DIGITE O CEP{ba}: ')
    a = requests.get(f'https://viacep.com.br/ws/{cep}/json')
    cp = a.json()

    print(f'{cia}CEP{ba}: {cp["cep"]}')
    print(f'{cia}LOGRADOURO{ba}: {cp["logradouro"]}')
    print(f'{cia}COMPLEMENTO{ba}: {cp["complemento"]}')
    print(f'{cia}BAIRRO{ba}: {cp["bairro"]}')
    print(f'{cia}LOCALIDADE{ba}: {cp["localidade"]}')
    print(f'{cia}UF{ba}: {cp["uf"]}')
    print(f'{cia}IBGE{ba}: {cp["ibge"]}')
    print(f'{cia}GIA{ba}: {cp["gia"]}')
    print(f'{cia}DDD{ba}: {cp["ddd"]}')
    print(f'{cia}SIAF{ba}: {cp["siafi"]}')
Cep()