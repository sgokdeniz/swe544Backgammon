import socket               
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import XML, fromstring, tostring  , parse
from Game import Game


global gamex

def protocolSelector(protocol,game,conn):
   
    
   
    #xmlelement = ET.fromstring(protocol)
    xmlelement=XML(protocol)
    print xmlelement.tag
    if(xmlelement.tag=="CLOGIN"):
        a_lst = xmlelement.findall("username")
        val=''
        for node in a_lst:
            val=node.attrib["usr"]
            print val
        srvau(val,game,conn)
        
    


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
            a=protocolSelector(data,gamex,conn)
            
            print type(conn)
            
            #conn.sendall('hell')
            
        except:
            pass
    
        
        if not data: break
        
    conn.close()


    