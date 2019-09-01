import socket
serveraddr=""
conaddr=""
renderip=0
renderport=1024
#server reply to controller after set up
def replytocon(message,serveraddr,conaddr):
    render_socket.sendto(str.encode("Connection established between Render"), conaddr)
    render_socket.sendto(str.encode("Enter 'sttn [Filename]' to stream the file"), conaddr)
    render_socket.sendto(str.encode("Enter 'li' to get streamable list"), conaddr)
    print("Connection established between Controller")
    listener(message,serveraddr,conaddr)
    
#connection to server
def conntoser(message,serveraddr,conaddr):
    print("Connection request recieved from server")
    message = message.replace("c2s","")
    medport = message[-4:]
    medaddr = message.replace(medport,"")
    saddr = (medaddr, int(str(medport),10))
    print ("Connection established between server")
    serveraddr = saddr
    render_socket.sendto(str.encode("Connection established"), saddr)
    listener(message,serveraddr,conaddr)
    
#connection to Con
def conntocon(message,serveraddr,conaddr):
    print("Connection request recieved from Controller")
    message = message.replace("c2c","")
    conport = message[-4:]
    conaddr = message.replace(conport,"")
    conaddr = (conaddr, int(conport,10))
    replytocon(message,serveraddr,conaddr)
    print("Message sent to Controller!")

#Request to play the file
def request_to_play_file(message,serveraddr,conaddr):
    message = message.encode('utf-8')
    render_socket.sendto(message,serveraddr)
    print(serveraddr)
    print("Requesting file....")
    listener(message,serveraddr,conaddr)

#pausing the file
def servercommand(message,serveraddr,conaddr):
    render_socket.sendto(str.encode(message),serveraddr)
    listener(message,serveraddr,conaddr)

#sent the "get list" request to server
def set_list(message,serveraddr,conaddr):
    render_socket.sendto(str.encode("list"), serveraddr)
    listener(message,serveraddr,conaddr)

#setting up Connection listener
#IP based on device
#Port is set to 1024
print("Render booting...")

#creating render listener socket
render_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
render_socket.bind(('', renderport))
print("Render online, address and port:")
a=socket.gethostname()
print(socket.gethostbyname(a),renderport)
print("Ready for connection")

#Reciever(listener)"TCP4con"
def listener(message,serveraddr,conaddr):
    message = ""
    print("Currently awaits commonds ......")
    while True:
        message, address = render_socket.recvfrom(renderport)
        message = message.decode("utf-8")
        if "Paused, Please 'sss'(continue) or 'rsrs'(restart) "==message:
            print(message)
            message =""
        #determining what message is
        #connections
        if "c2c" in message:
            conntocon(message,serveraddr,conaddr)
        if "c2s" in message:
            conntoser(message,serveraddr,conaddr)
    
        #functions for controller
        if "sttn" in message:
            request_to_play_file(message,serveraddr,conaddr)
        if "ppp" in message:
            print ("Pause request sent")
            servercommand(message,serveraddr,conaddr)
        if "rsrs" in message:
            print ("Restart request sent")
            servercommand(message,serveraddr,conaddr)
        if "sss" in message:
            print ("Continue request sent")
            servercommand(message,serveraddr,conaddr)
        #parsing message(file) from server
        if "li" in message:
            set_list(message,serveraddr,conaddr)
        #used to print file list
        if "." in message:
            print(message)
        if "kek" in message:
            print("Currently awaits commonds ......")

        #sneding file
        if "ttttt" in message:
            message = message.replace("ttttt","")
            print(message)
        if "TTTTT" in message:
            message = "==End of file=="
            print(message)
            print("Currently awaits commonds ......")

listener(0,0,0)
