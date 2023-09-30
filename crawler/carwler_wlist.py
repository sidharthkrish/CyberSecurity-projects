#!/usr/bin/env python
import requests

def request(url):
    try:
        return requests.get("http://"+url)
    except:
        pass

def main():
    print("sniffer program using wordlist\n*********************\n")
    url=input("enter the base url without http://")
    filepath=input("enter the file path")
    subdomains=[]

    with open(filepath,"r") as wlist:
     for line in wlist:
        word=line.strip()
        test=url+"/"+word
        resp=request(test)
        if resp:
            print("[+] URL FOUND"+test)
            subdomains.append(test)
        
