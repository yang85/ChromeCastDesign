import socket
import os
import time
print("Media server is booting...")
#listener port
serverport = 4096
tempport = 4098
#open sockets
ser_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ser_socket.bind(('', serverport))

#get the list at current directory 
def getlisting(saddr):
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    print("sending info to server")
    while files:
        message = files[0]
        message = message.encode('utf-8')
        ser_socket.sendto(message, saddr)
        del files[0]
    ser_socket.sendto("kek".encode('utf-8'), saddr)
    
#access file
def getfile(filename,saddr):
    ft = open(filename)
    tlines=ft.readlines()
    ft.close()
    ct=1
    total=len(tlines)+1
    sendfile(tlines,saddr,total,ct,filename)
    
#send accessed file
def sendfile(tlines,saddr,total,ct,filename):
    try :
        ser_socket.settimeout(0.1)
        message, address = ser_socket.recvfrom(serverport)
        message = message.decode("utf-8")
        if "ppp" in message:
            raise ValueError
    except ValueError:
        pud(tlines, ct, total,saddr,filename)
    except socket.timeout:
        print("Sending file "+str(ct)+"/"+str(total))
        if tlines:
            message = tlines[0]
            del tlines[0]
            message = "ttttt"+message
            newmes = message.encode('utf-8')
            ser_socket.sendto(newmes, saddr)
            ct+=1
            sendfile(tlines,saddr,total,ct,filename)
        else:
            message = "TTTTT"
            newmes = message.encode('utf-8')
            ser_socket.sendto(newmes, saddr)
            print("===Completed===")
            wl(message,saddr)
            
#if pause is input
def pud(tlines, ct, total,saddr,filename):
    message = "Paused, Please 'sss'(continue) or 'rsrs'(restart) "
    message = message.encode('utf-8')
    ser_socket.sendto(message, saddr)
    ser_socket.settimeout(100)
    message = ""
    message, address = ser_socket.recvfrom(serverport)
    message = message.decode("utf-8")
    if "rsrs" in message:
        print("Starting from beginning.....")
        getfile(filename,saddr)
    elif "sss" in message:
        sendfile(tlines,saddr,total,ct,filename)
    else:
        message = "Paused, Please 'sss'(continue) or 'rsr'(restart) "
        message = message.encode('utf-8')
        ser_socket.sendto(message, saddr)
            
#connects to Render()    
def ContoRen():
    #parsing address into message
    saddr = input("Enter the IP printed on Render end: ")
    sport = input("Enter the Port printed on Render end: ")

    #getting servers address
    c="c2s"
    a=socket.gethostbyname(socket.gethostname())
    targetaddr = a+str(serverport)
    targetaddr = targetaddr+c
    bitmes = targetaddr.encode('utf-8')

    #send the info to render
    saddr = (saddr, int(sport,10))
    ser_socket.sendto(bitmes, saddr)
    print("Connection request sent!")
    #awaits return from server
    while True:
        message, address = ser_socket.recvfrom(serverport)
        message = message.decode("utf-8")
        print (message)
        if "established" in message:
            wl(0,saddr)

#listener 
def wl(message,saddr):
    print("Currently awaits commonds from Render......")
    ser_socket.settimeout(10000)
    while True:
        message, address = ser_socket.recvfrom(serverport)
        message = message.decode("utf-8")
        if message == "list":
            getlisting(saddr)
            wl(message,saddr)
        if "sttn" in message:
            filename = message.replace("sttn ", "")
            message = ""
            labels=0
            getfile(filename,saddr)
        if "resume" in message:
            message = ""
            pud(filename,labels)
ContoRen()
