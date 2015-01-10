from Tkinter import *
import socket 
import xml.etree.ElementTree as ET
class MainMenu:
    global root
    
    def splay(self,usr):
        print usr
        pass
        
    def cplay(self,username,ip,port):
        self.socket=self.connect(ip,port)
        log = ET.Element("CPLAY")
        ET.SubElement(log, "username", usr=username)
        data=ET.tostring(log, encoding='UTF-8')
        self.socket.sendall(data)
        data = self.socket.recv(1024)
        print data
        self.socket.close()
    
    def connect(self,ip,sport):
        s = socket.socket()
        host = ip 
        port = int(sport) 
        s.connect((host, port))
        return s
        
    def __init__(self,username,ip,port):
        root = Tk()
        root.title("Main Menu")
        root.geometry("200x100")
        Label(text='Your Username:').grid(row=0,column=0)
        Label(text=username).grid(row=0,column=1)
        btPlay=Button(text='Play', command=lambda: self.cplay(username,ip,port))
        btPlay.grid(row=1,column=0)
        btWatch=Button(text='Watch', command=lambda: cwatch(username))
        btWatch.grid(row=1,column=1)
        root.mainloop()
    
    