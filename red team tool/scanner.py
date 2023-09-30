import scapy.all as scapy

def scanner(ip):
    req=scapy.ARP(pdsr=ip)
    bcast=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    req_bcast=bcast/req
    answered=scapy.src(req_bcast, timeout=1,verbose=False)[0]

    clients=[]
    for x in answered:
        d={"ip":x[1].psrc,"mac":x[1].hwsrc}
        clients.append(d)
    return clients

def res(clients):
    print("IP"+"\t\t\t"+"MAC\n.........................")
    for c in clients:
        print(c["ip"]+"\t\t"+c["mac"])
    
def main():
    print("Scanner program\n................................")
    ip=input("enter ip to scan")
    client_list=scanner(ip)
    res(client_list)
    