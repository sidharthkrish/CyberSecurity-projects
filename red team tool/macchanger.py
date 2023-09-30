#!/usr/bin/env python

import subprocess
import optparse
import re

from requests import options

def get_input():
    p=optparse.OptionParser()
    p.add_option("-i",dest="intf",help="mention interface")
    p.add_option("-m",dest="newaddr",help="mention new addres for MAC")
    (options, arguments)=p.parse_args()
    return options

def changer(intf, newaddr):
    subprocess.call(["ifconfig",intf,"down"])
    subprocess.call(["ifconfig",intf,"hw","ether",newaddr])
    subprocess.call(["ifconfig",intf,"up"])

def old_mac(intf):
    cmd=subprocess.check_output(["ifconfig",intf])
    res=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",cmd)
    if res:
        return res.group(0)

def main():
    args=get_input()
    x=old_mac(args.intf)
    changer(args.intf,args.newaddr)
    y=old_mac(args.intf)
    if x!=y:
        print("changed successfully")
