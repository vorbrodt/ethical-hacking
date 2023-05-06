import socket

def scan(target, ports):
    print("\n" + "Starting scan for " + str(target))
    for port in range(1, ports):
      scan_port(target, port);

def scan_port(ipaddress, port):
    try:
      #initiate socket object
      sock = socket.socket()
      #connect to target
      ret = socket.connect((ipaddress, port))
      print("[+]Port Opened " + str(port))
      sock.close()
    except:
      pass


targets = input("[*] Enter targets to scan: ") #e.g. 192.168.1.1, 192.168.1.5
ports = int(input("[*] Enter number of ports to scan: "))

#check if multiple targets specified
if "," in targets:
  print("[*] Scanning multiple targets")
  for ip_addr in targets.split(","):
    scan(ip_addr.strip(" "), ports)
else:
  scan(targets, ports)
    