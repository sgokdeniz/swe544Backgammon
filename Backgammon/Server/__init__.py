import socket               
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import XML, fromstring, tostring  , parse
from Game import Game
import threading
import random

global gamex

def protocolParser(protocol,game,conn):
   
   
    #xmlelement = ET.fromstring(protocol)
    
    xmlelement=XML(protocol)
    print xmlelement.tag
    if(xmlelement.tag=="CLOGIN"):
        a_lst = xmlelement.findall("username")
        val=''
        for node in a_lst:
            val=node.attrib["usr"]
            print val
        threading.Thread(target=srvau(val,game,conn)).start()
        
    elif(xmlelement.tag=="CPLAY"):
        a_lst = xmlelement.findall("username")
        print 'a_lst'
        val=''
        for node in a_lst:
            val=node.attrib["usr"]
            print val
       
        threading.Thread(target=splay(val,game,conn)).start()
        
    elif(xmlelement.tag=="CDICE"):
        print xmlelement.tag
        a_lst = xmlelement.findall("username")
        
        val=''
        for node in a_lst:
            val=node.attrib["usr"]
            print val
       
        sdice(val,game,conn)


def srvau(val,game,conn):
    slogin=game.addUser(val)
    if(slogin==True):
        slog = ET.Element("SRVAU")
        ET.SubElement(slog, "username", auth='OK')
        conn.sendall(ET.tostring(slog, encoding='UTF-8'))
    elif(slogin==False):
        slog = ET.Element("SRVAU")
        ET.SubElement(slog, "username", auth='FAIL')
        conn.sendall(ET.tostring(slog, encoding='UTF-8'))

def splay(val,game,conn):
    sply=game.delegatePlayer(val)
    splay = ET.Element("SPLAY")
    ET.SubElement(splay, "game", gameId=str(sply))
    ET.SubElement(splay, "state", play='OPEN')
    conn.sendall(ET.tostring(splay, encoding='UTF-8'))


def sdice(val,game,conn):
    rollx = random.randint(1, 6)
    rolly = random.randint(1, 6)
    print rollx
    sdice = ET.Element("SDICE")
    ET.SubElement(sdice, "d1", value=str(rollx))
    ET.SubElement(sdice, "d2", value=str(rolly))
    ET.SubElement(sdice, "username", value=str(rolly))
    print sdice
    conn.sendall(ET.tostring(sdice, encoding='UTF-8'))
HOST = ''                 
PORT = 8666              
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
gamex=Game()
print 'Listening to port 8666'
s.listen(1)
while True: 
    conn, addr = s.accept()
    a=''
    print 'Connected by', addr
    while True:
        data = conn.recv(1024)
        print type(data)
        try:
            print 'dd'
            a=protocolParser(data,gamex,conn)
            
            print type(conn)
            
            #conn.sendall('hell')
            
        except:
            pass
    
        
        if not data: break
        
    conn.close()


    