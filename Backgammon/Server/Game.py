
class Game:
    global userlist
    def __init__(self):
        self.userlist=list()
        
    def addUser(self,username):
        print len(self.userlist)
        print username
        if(len(self.userlist)==0):
            self.userlist.append(username)
            print len(self.userlist)
            return True
        else:
            
            for i in self.userlist:
                
                
                if(username==i):
                    return False
                 
                else:
                    print i
                    self.userlist.append(username)
                    return True
               
    def getUserlist(self):
        return self.userlist
            
        
    
        
        
    