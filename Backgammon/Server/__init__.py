import socket               
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import XML, fromstring, tostring  , parse

def protocolSelector(protocol):
   
    
    pro=protocol.replace("<?xml version='1.0' encoding='UTF-8'?>"," ")
    #xmlelement = ET.fromstring(protocol)
    xmlelement=XML(protocol)
    a_lst = xmlelement.findall("username")
    for node in a_lst:
        node.attrib["usr"]

HOST = ''                 
PORT = 8666              
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
print 'Listening to port 8666'
s.listen(1)
while True: 
    conn, addr = s.accept()
    print 'Connected by', addr
    while True:
        data = conn.recv(1024)
        print data
        try:
            protocolSelector(data)
        except:
            pass
    
        
        if not data: break
        conn.sendall(data)
    conn.close()


    