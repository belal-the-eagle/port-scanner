#!/usr/bin/python3
import socket
import sys
import pyfiglet
from colorama import Fore,Style
def scan(ip,port):
    print("")
    try:
       s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
       s.settimeout(1.0)
       m=s.connect_ex((ip,port))
       if m == 0:
          print(f"{Fore.GREEN}[+] Port {port} is open")
       else:
          print(f"{Fore.RED}[-] Port {port} is closed")
    except Exception as e:
       print(f"Error :{e}")
    finally:
       s.close()
def custom_scan(ip,s_port,f_port):
    banner()
    print("")
    for x in range(s_port,f_port+1):
       s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
       s.settimeout(1.0)
       m = s.connect_ex((ip,x))
       if m == 0:
          s.close()
          print(f"{Fore.GREEN}[+] Port {x} is open")
def banner():
    ban=pyfiglet.figlet_format("Port Scanner")
    print(f"{Fore.CYAN}{ban}{Style.RESET_ALL}")
    print(f"          {Fore.YELLOW}BELAL@NADA{Style.RESET_ALL}")
if len(sys.argv) == 3:
   ip = sys.argv[1]
   port = int(sys.argv[2])
   banner()
   scan(ip,port)
if len(sys.argv) == 4:
   ip = sys.argv[1]
   s_port = int(sys.argv[2])
   f_port = int(sys.argv[3])
   custom_scan(ip,s_port,f_port)
if len(sys.argv) != 3 or 4:
   banner()
   print(f"{Fore.MAGENTA}Usage :: python port-scanner.py <target_ip> <target_port>{Style.RESET_ALL}")
   print(f"{Fore.MAGENTA}Usage :: python port-scanner.py <target_ip> <from_port> <to_port> {Style.RESET_ALL}")
   sys.exit()
