from Tkinter import *
import socket 
import xml.etree.ElementTree as ET
from GameBoard import GameBoard
class MainMenu:
    global root
    
    def cwtch(self,username,ip,port):
        self.socket=self.connect(ip,port)
        log = ET.Element("CDICE")
        ET.SubElement(log, "username", usr=username)
        data=ET.tostring(log, encoding='UTF-8')
        self.socket.sendall(data)
        data = self.socket.recv(1024)
        print data
        xmlelement=ET.XML(data)
        print xmlelement.tag
        if(xmlelement.tag=="SDICE"):
            a_lst = xmlelement.findall("d1")
            val=''
            for node in a_lst:
                val=node.attrib["value"]
                print val
        
        self.closeWindow(self.root)
        GameBoard(username,ip,port,val)
        self.socket.close()
        
    def cplay(self,username,ip,port,sock):
        sock=self.connect(ip,port)
        log = ET.Element("CPLAY")
        ET.SubElement(log, "username", usr=username)
        data=ET.tostring(log, encoding='UTF-8')
        sock.sendall(data)
        data = sock.recv(1024)
        print data
        xmlelement=ET.XML(data)
        print xmlelement.tag
        if(xmlelement.tag=="SPLAY"):
            a_lst = xmlelement.findall("game")
            val=''
            for node in a_lst:
                val=node.attrib["gameId"]
                print val
        self.closeWindow(self.root)
        GameBoard(username,ip,port,val,sock)
        
    
    def connect(self,ip,sport):
        s = socket.socket()
        host = ip 
        port = int(sport) 
        s.connect((host, port))
        return s
    def closeWindow(self,window):
        self.root.destroy()    
    def __init__(self,username,ip,port,s):
        self.root = Tk()
        self.root.title("Main Menu")
        self.root.geometry("200x100")
        Label(text='Your Username:').grid(row=0,column=0)
        Label(text=username).grid(row=0,column=1)
        btPlay=Button(text='Play', command=lambda: self.cplay(username,ip,port,s))
        btPlay.grid(row=1,column=0)
        btWatch=Button(text='Watch', command=lambda: self.cwtch(username,ip,port))
        btWatch.grid(row=1,column=1)
        self.root.mainloop()
    
    