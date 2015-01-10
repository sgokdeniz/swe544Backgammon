from GameDetails import GameDetails
class Game:
    global userlist
    global gamelist
    global gameNum
    def __init__(self):
        self.userlist=list()
        self.gamelist=list()
        self.gameNum=0;
        
    def addUser(self,username):
        print len(self.userlist)
        print username
        if(len(self.userlist)==0):
            self.userlist.append(username)
            print len(self.userlist)
            return True
        else:
            if username in self.userlist:
                return False
            else:
                self.userlist.append(username)
                return True
           
    def getUserlist(self):
        return self.userlist
    def setupGame(self,gameNumber,username):
        self.gameNum=self.gameNum+1
        gameSet=GameDetails(gameNumber,username)
        self.gamelist.append(gameSet)
        
        
        print len(self.gamelist)
        return type(gameSet)
        #=======================================================================
        # gameSet=GameDetails(gameNumber,username)
        # self.gamelist[self.gameNum]=gameSet
        # self.gameNum=self.gameNum+1
        # print self.gameNum 
        #=======================================================================
              
    def delegatePlayer(self,username):
        
        if(len(self.userlist)%2==1):
            print 'OKK'
            
            a=self.setupGame(self.gameNum,username)
            return a
           
        elif(len(self.userlist)==1):
            print 'OK'
            #----------------------------- self.setupGame(self.gameNum,username)
        else:
            pass
                
    
        
    def availableGame(self):
        pass
    def getGameNumber(self):
        return self.gameNum
            
    
           
