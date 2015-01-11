from Tkinter import *
import socket 
import xml.etree.ElementTree as ET
class GameBoard:
    global root
    
    def cmove(self,usr):
        print usr
        pass
        
    def cdice(self,username,ip,port):
        print port,ip
        self.socket=self.connect(ip,port)
        log = ET.Element("CDICE")
        ET.SubElement(log, "username", usr=username)
        data=ET.tostring(log, encoding='UTF-8')
        print 'xx'
        self.socket.sendall(data)
        dat = self.socket.recv(1024)
        print dat
        self.socket.close()
        
    def cswma(self,username,ip,port):
        pass
    
    def connect(self,ip,sport):
        s = socket.socket()
        host = ip 
        port = int(sport) 
        s.connect((host, port))
        return s
        
    def __init__(self,username,ip,port,gameId):
        root = Tk()
        root.title("Game")
        root.geometry("600x500")
        Label(text='Your Username:').grid(row=0,column=0)
        Label(text=username).grid(row=0,column=1)
        Label(text='Your GameID:').grid(row=0,column=2)
        Label(text=gameId).grid(row=0,column=3)
        btPlay=Button(text='Throw dice', command=lambda: self.cdice(username,ip,port))
        btPlay.grid(row=1,column=0)
        btWatch=Button(text='Move', command=lambda: self.cmove(username))
        btWatch.grid(row=1,column=1)
        root.mainloop()