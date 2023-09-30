import socket 


# splitting targets as individual ports 

def scan(target,ports):
    print("\n"+'Starting Scan For'+str(target))
    for port in range(1,ports):
        scan_port(target,port)

#scan function

def scan_port(ipaddress,port):
    try:
        sock = socket.socket()           
        sock.connect((ipaddress, port)) 
        banner=sock.recv(1024)
        print("[+]Open Port"+ str(port)+banner)
        sock.close()                  
    except:
        pass

# main driver code :

def main():
    print("***PORT SACNNER***\nchoose an option\n1.single ip and single port\n.2.multiple ips and ports/n")
    ch=int(input())
    if ch==1:
        targets = input("[*] Enter IP To Scan: ")
        ports = int(input("[*] Enter the port number: "))
        scan(targets,ports)


    elif ch==2:
        targets = input("[*] Enter Targets To Scan(Split By ,): ")
        ports = int(input("[*] How Many Ports To Scan: "))


    if ',' in targets:
        print("[*] Scanning Targets")
        for ip_addr in targets.split(','):
            scan(ip_addr.strip(' '),ports)
    else:
        scan(targets,ports)

