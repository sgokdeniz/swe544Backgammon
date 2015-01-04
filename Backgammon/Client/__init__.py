from Tkinter import *
from tkMessageBox import *
import socket 
import xml.etree.ElementTree as ET
from MainMenu import MainMenu

global master
master = Tk()

def callback(usr,ip,port):
    
    print usr , ip , port
    connect(usr , ip , port)
    
def connect(username,ip,sport):
    s = socket.socket()
    host = ip 
    port = int(sport) 
    s.connect((host, port))
    data = clogin(username)
    s.sendall(data)
    data = s.recv(1024)
    s.close()
    xmlelement=ET.XML(data)
    print xmlelement.tag
    if(xmlelement.tag=="SRVAU"):
        a_lst = xmlelement.findall("username")
        val=''
        for node in a_lst:
            val=node.attrib["auth"]
            print val
        if(val=='FAIL'):
            showwarning('Warning','Try another username!!')
        else:
            closeWindow(master)
            MainMenu(username)   
            
    #print 'Received', repr(data)
           
def clogin(username):
    log = ET.Element("CLOGIN")
    ET.SubElement(log, "username", usr=username)
    
   
    #log.attrib["username"] = username
   
    
    return  ET.tostring(log, encoding='UTF-8')

def closeWindow(root):
    root.destroy()
    
    
Label(text='Username:').grid(row=0,column=0)
username=Entry(master)
username.grid(row=0,column=1)
Label(text='IP & Port number:').grid(row=1,column=0)
ipaddress=Entry(master)
ipaddress.grid(row=1,column=1)
port=Entry(master)
port.grid(row=1,column=2)
bt=Button(text='Connect', command=lambda: callback(username.get(),ipaddress.get(),port.get()))
bt.grid(row=2,column=2)


master.mainloop()