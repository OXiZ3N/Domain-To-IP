import os
import socket
from multiprocessing.dummy import Pool

os.system('cls' if os.name == 'nt' else 'clear')
print('''
\t\t ██████╗ ██╗  ██╗██╗███████╗██████╗ ███╗   ██╗
\t\t██╔═══██╗╚██╗██╔╝██║╚══███╔╝╚════██╗████╗  ██║
\t\t██║   ██║ ╚███╔╝ ██║  ███╔╝  █████╔╝██╔██╗ ██║
\t\t██║   ██║ ██╔██╗ ██║ ███╔╝   ╚═══██╗██║╚██╗██║
\t\t╚██████╔╝██╔╝ ██╗██║███████╗██████╔╝██║ ╚████║
\t\t ╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝╚═════╝ ╚═╝  ╚═══╝
\t\t                Domain_To_IP                                          
      ''')

def get_ip(website):
    try:
        address = socket.gethostbyname(website)
        print('\t\t [+] Grabbed IP : ' + address)
        with open('IPs.txt', 'a') as f:
            f.write(address + '\n')
    except Exception as e:
        print('\t\t [-] ' + website + ' : error')

def process_sites(sites):
    pool = Pool(150)
    pool.map(get_ip, sites)
    pool.close()
    pool.join()

website_list = input('\t\t[!] Domain List: ')

with open(website_list) as f:
    sites = [line.strip().replace('http://', '').replace('https://', '') for line in f]

process_sites(sites)
