import socket
print("Controller is booting...")
#listener port
conport=2048

def awaits(raddr):
    while True:
        me=input("Enter your command: ")
        con_socket.sendto(str.encode(me), raddr)
#open sockets
con_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
con_socket.bind(('', conport))

#parsing address into message
raddr = input("Enter the IP printed on Render end: ")
rport = input("Enter the Port printed on Render end: ")

#getting controller's address
c="c2c"
a=socket.gethostbyname(socket.gethostname())
targetaddr = a+str(conport)
targetaddr = targetaddr+c
bitmes = targetaddr.encode('utf-8')

#send the info to render
raddr = (raddr, int(rport,10))
con_socket.sendto(bitmes, raddr)
print("Connection request sent!")
while True:
    message, address = con_socket.recvfrom(conport)
    message = message.decode("utf-8")
    print (message)
    if "streamable" in message:
        print("Enter 'ppp' to pause the file")
        awaits(raddr)
        
