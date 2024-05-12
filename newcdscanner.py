import pyfiglet
import socket
import threading
import concurrent.futures
import datetime
import argparse


parser = argparse.ArgumentParser(prog='newcdscanner.py', usage='%(prog)s [Target] [Port]',epilog="Example: newcdscanner.py google.com 1-10000  fast.py github.com all ")
parser.add_argument("target", help = "[target ip]")
parser.add_argument("port", help = "[port] (default = 1-1000)",default=1,  nargs = '?') 
args = parser.parse_args()
ip=args.target
nport=args.port
if nport==1:
        start=1
        end=1000

elif nport== "all":
        start=1
        end=65535
else:
        
        start,end= nport.split("-")
        start= int(start)
        end= int(end)



print("-" * 70)
print("[Dev by NewCode]")
print("""                ...
               ;::::;
             ;::::; :;
           ;:::::'   :;
          ;:::::;     ;.
         ,:::::'       ;           OOO
         ::::::;       ;          OOOOO
         ;:::::;       ;         OOOOOOOO
        ,;::::::;     ;'         / OOOOOOO
      ;:::::::::`. ,,,;.        /  / DOOOOOO
    .';:::::::::::::::::;,     /  /     DOOOO
   ,::::::;::::::;;;;::::;,   /  /        DOOO
  ;`::::::`'::::::;;;::::: ,#/  /          DOOO
  :`:::::::`;::::::;;::: ;::#  /            DOOO
  ::`:::::::`;:::::::: ;::::# /              DOO
  `:`:::::::`;:::::: ;::::::#/               DOO
   :::`:::::::`;; ;:::::::::##                OO
   ::::`:::::::`;::::::::;:::#                OO
   `:::::`::::::::::::;'`:;::#                O
    `:::::`::::::::;' /  / `:#
     ::::::`:::::;'  /  /   `#""")
print("\n")

def date_time():
	return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

print_lock = threading.Lock()


# translate hostname to IPv4
targetip = socket.gethostbyname(ip)

# For information

print("[Scanning Target ]- {} ({})".format(ip,targetip))
print("[Scan started ]- [{}]".format(date_time()))


print("\n      |Ip|\t\t|Open Port|\t\t|State|")
print("-" * 55)
#Scaning
def scan(ip,port):
    scanner= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)

    try:
        scanner.connect((ip,port))
        scanner.close()

        with print_lock:
            print("{}\t\t{}\t\tOpen".format(targetip,port))

    except:
        pass

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    # will scan ports between 1 to 65,535
    for port in range(start,end):
        executor.submit(scan, ip, port + 1)


print("\n[Scan finished ! Thanks for using - ][{}]".format(date_time()))
print("-" * 70)
