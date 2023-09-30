import server
import macchanger
import rookie_port_scanner
import scanner

print("select choice to start the program\n 1.mac changer\n2.server of backdoor\n3.port scanner\n4.sniffer\n5.exit\n")
ch=str(input())
if ch==1:
    macchanger.main()
elif ch==2:
    server.main()
elif ch==3:
    rookie_port_scanner.main()
elif ch==4:
    scanner.main()
elif ch==5:
    exit()
else:
    print("select one of the choices")

