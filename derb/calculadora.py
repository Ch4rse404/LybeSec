import os
while True:
   print("""
   /\  \     /\  \     /\__\     /\  \     /\__\     /\__\     /\  \     /\  \     /\  \     /\  \     /\  \  
  /::\  \   /::\  \   /:/  /    /::\  \   /:/ _/_   /:/  /    /::\  \   /::\  \   /::\  \   /::\  \   /::\  \ 
 /:/\:\__\ /::\:\__\ /:/__/    /:/\:\__\ /:/_/\__\ /:/__/    /::\:\__\ /:/\:\__\ /:/\:\__\ /::\:\__\ /::\:\__\
 \:\ \/__/ \/\::/  / \:\  \    \:\ \/__/ \:\/:/  / \:\  \    \/\::/  / \:\/:/  / \:\/:/  / \;:::/  / \/\::/  /
  \:\__\     /:/  /   \:\__\    \:\__\    \::/  /   \:\__\     /:/  /   \::/  /   \::/  /   |:\/__/    /:/  / 
   \/__/     \/__/     \/__/     \/__/     \/__/     \/__/     \/__/     \/__/     \/__/     \|__|     \/__/""")
    operacao = input('Qual operacao (+, -, *, /)? ou \'Q\' para sair ')
    if operacao == 'Q' or operacao == 'q':
        break

    elif operacao == '+' or operacao == '-' or operacao == '*' or operacao == '/':

        x = int(input('Digite o primeiro numero: '))

        y = int(input('Digite o segundo numero: '))

        if operacao == '+':
            result = x + y

        elif operacao == '-':
            result = x - y

        elif operacao == '*':
            result = x * y

        elif operacao == '/':
            result = x / y

        else:
            print('Operação Invalida')

        print(result)

        input('PRESS ENTER')
        os.system('clear')

    else:
        print('Operação Invalida')
        input('PRESS ENTER')
        os.system('clear')