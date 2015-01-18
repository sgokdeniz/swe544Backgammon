from Tkinter import *
import socket 
import xml.etree.ElementTree as ET

class GameBoard:
    global root
    
    def cmove(self,usr):
        print usr
        pass
        
    def cdice(self,username,ip,port,s):
        print port,ip
        log = None
        log = ET.Element("CDICE")
        ET.SubElement(log, "username", usr=username)
        data=ET.tostring(log, encoding='UTF-8')
        print data
        s.sendall(data)
        data = s.recv(1024)
        print data
        xmlelement=ET.XML(data)
        if(xmlelement.tag=="SDICE"):
            a_lst = xmlelement.findall("d1")
            d1,d2='',''
            for node in a_lst:
                d1=node.attrib["value"]
                print d1
            b_lst = xmlelement.findall("d2")
            for node in b_lst:
                d2=node.attrib["value"]
                print d2
        
    def cswma(self,username,ip,port):
        pass
    
        
    def __init__(self,username,ip,port,gameId,sock):
        print username,ip,port,gameId
        root = Tk()
        root.title("Game")
        root.geometry("600x500")
        Label(text='Your Username:').grid(row=0,column=0)
        Label(text=username).grid(row=0,column=1)
        Label(text='Your GameID:').grid(row=0,column=2)
        Label(text=gameId).grid(row=0,column=3)
        Label(text='User:').grid(row=0,column=4)
        Label(text=gameId).grid(row=0,column=5)
        btDice=Button(text='Throw dice', command=lambda: self.cdice(username,ip,port,sock))
        btDice.grid(row=1,column=0)
        btMove=Button(text='Move', command=lambda: self.cmove(username))
        btMove.grid(row=1,column=1)
        root.mainloop()