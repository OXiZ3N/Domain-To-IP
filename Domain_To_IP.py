import os
import socket

os.system('cls')
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

website_list = input('\t\t[!] Domain List: ')

with open(website_list) as f:
    for website in f:
        website = website.strip()
        if website.startswith('http://'):
            website = website[7:]
        get_ip(website)