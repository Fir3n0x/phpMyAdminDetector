import sys
import socket
import math
import requests

def byte_to_dec(byte):
    byte_dec = 0
    for i in range(8):
        byte_dec += int((math.pow(2,i) * int(byte[-(i+1)])))
    return byte_dec

def ip_to_binary(ip_address):
    try:
        bynary_representation = socket.inet_aton(ip_address)
        return ''.join(f'{byte:08b}' for byte in bynary_representation)
    except socket.error:
        return "Adresse IP invalid"
        exit(0)

def binary_to_ip(binary_address):
    try:
        forth_byte = binary_address[:8] #bit poids fort
        thrd_byte = binary_address[8:16]
        snd_byte = binary_address[16:24]
        fst_byte = binary_address[24:32] #bit poids faible
        #print(forth_byte + " " + thrd_byte + " " + snd_byte + " " + fst_byte)
        return str(byte_to_dec(forth_byte)) + "." + str(byte_to_dec(thrd_byte)) + "." + str(byte_to_dec(snd_byte)) + "." + str(byte_to_dec(fst_byte))
    except:
        return "Binary IP invalid"
        exit(0)

def increment_binary_string(binary_address):
    #int() prend un nombre et une base (ici base de 2 binaire)
    return '{:032b}'.format(1+int(binary_address,2))


def main():

    target_ip = []
    
    cidr = sys.argv[1]
    print("Searching phpmyadmin through " + cidr + "...\n")


    addr = ip_to_binary(cidr[:(cidr.find("/"))])
    mask = int(cidr[(cidr.find("/")+1):])
    #print(addr + " " + mask)
    #print(binary_to_ip(addr))
    #addr = binary_to_ip(addr)

    
    
    for i in range(int(math.pow(2,(32-mask)))):
        try:
            print("http://" + binary_to_ip(addr) + "/phpmyadmin/")
            response = requests.get("http://" + binary_to_ip(addr) + "/phpmyadmin/",timeout = 0.3)
            target_ip.append(binary_to_ip(addr))
            print(binary_to_ip(addr) + " --> " + str(response.status_code))
        except requests.RequestException:
            print(binary_to_ip(addr) + " NOT")
        except KeyboardInterrupt:
            print("\nStopped by the user.")
            sys.exit(0)

        addr = increment_binary_string(addr)

    print("Possible phpmyadmin IP machine:")
    for ip in target_ip:
        print(ip)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("""
This script will look for phpmyadmin server in the network according to the CIDR given
Usage: script.py 192.168.1.0/24
        """)
        sys.exit(0)
    else:
        main()