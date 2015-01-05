from Tkinter import *

class MainMenu:
    global root
    
    def cplay(self,usr):
        print usr
        pass
        
    def splay(self,usr):
        pass
    
    def __init__(self,username):
        root = Tk()
        root.title("Main Menu")
        root.geometry("200x100")
        Label(text='Your Username:').grid(row=0,column=0)
        Label(text=username).grid(row=0,column=1)
        btPlay=Button(text='Play', command=lambda: self.cplay(username))
        btPlay.grid(row=1,column=0)
        btWatch=Button(text='Watch', command=lambda: cwatch(username))
        btWatch.grid(row=1,column=1)
        root.mainloop()
    
    