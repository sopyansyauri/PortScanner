import socket

def scan(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        serviceVersion =  sock.recv(1024)
        serviceVersion = serviceVersion.decode("utf-8")
        serviceVersion = serviceVersion.strip("\n")
        print(f"Port {str(port)} is open", end="     ")
        print(serviceVersion)
    except ConnectionRefusedError:
        print(f"Port {str(port)} is closed")
    except UnicodeDecodeError:
        print(f"Port {str(port)} is open")

target = input("Target: ")
port = input("Port: ")

if ("," in port):
    portlist = port.split(",")
    for port in portlist:
        scan(target, int(port))
elif "-" in port:
    portrange = port.split("-")
    start = int(portrange[0])
    end = int(portrange[1])
    for port in range(start, end+1):
        scan(target, int(port))
else:
    scan(target, int(port))

