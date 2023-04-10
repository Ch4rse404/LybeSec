import progressbar, os, time
from colorama import init, Fore, Back, Style
init(autoreset=True)

def animated_marker():
    widgets = ['\033[94m[\033[97m#\033[94m]\033[97mLoading: ', progressbar.AnimatedMarker()]
    bar = progressbar.ProgressBar(widgets=widgets).start()

    for i in range(50):
        time.sleep(0.1)
        bar.update(i)

def cls():
    os.system("clear||cls")

cls()
def banner():
    print("""
            \033[94m [ \033[0m \033[1;37;41mTekShell generator reverse shell \033[0m \033[94m ] \033[0m
\033[1;49;35m████████╗███████╗██╗  ██╗\033[4;49;96m███████╗██╗  ██╗███████╗██╗     ██╗\033[0m
\033[1;49;35m╚══██╔══╝██╔════╝██║ ██╔╝\033[4;49;96m██╔════╝██║  ██║██╔════╝██║     ██║\033[0m
\033[1;49;35m   ██║   █████╗  █████╔╝ \033[4;49;96m███████╗███████║█████╗  ██║     ██║\033[0m
\033[1;49;35m   ██║   ██╔══╝  ██╔═██╗ \033[4;49;96m╚════██║██╔══██║██╔══╝  ██║     ██║\033[0m
\033[1;49;35m   ██║   ███████╗██║  ██╗\033[4;49;96m███████║██║  ██║███████╗███████╗███████╗\033[0m
\033[1;49;35m   ╚═╝   ╚══════╝╚═╝  ╚═╝\033[4;49;96m╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝\033[0m
            \033[1;37;41mCodded By: CharseSec\033[0m - \033[1;37;41mLybeSec Group\033[0m""")

banner()

print("")
print("""                    \033[1;49;35m[ 1 ] \033[4;49;96mGERAR SHELL\033[0m
                    \033[1;49;35m[ 2 ] \033[4;49;96mSAIR\033[0m """)
print("")

opc = input("\033[1;37;41mDigite sua opcao >>\033[0m")

if opc == '1':
    cls()
    from modulos import tek2
    animated_marker()
if opc == '2':
    os.system("exit")