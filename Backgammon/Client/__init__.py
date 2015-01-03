from Tkinter import *
from tkMessageBox import *
import socket 


def callback(usr,ip,port):
    
    print usr , ip , port
    connect(usr , ip , port)
    
def connect(username,ip,sport):
    s = socket.socket()
    host = ip 
    port = int(sport) 
    s.connect((host, port))
    s.sendall('Hello, world')
    data = s.recv(1024)
    s.close()
    print 'Received', repr(data)
           
   
master = Tk()
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