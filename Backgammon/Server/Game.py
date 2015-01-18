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
        
        return self.gameNum
              
    def delegatePlayer(self,username):
        
        if(len(self.userlist)%2==1):
            print 'Waiting for another user'
            
            gameState=self.setupGame(self.gameNum,username)
            return gameState
           
        elif(len(self.userlist)==1):
            print 'OK'
            #----------------------------- self.setupGame(self.gameNum,username)
        else:
            print 'Waiting for '
            
            gameState=self.setupGame(self.gameNum,username)
            return gameState
                
    
        
    def availableGame(self):
        pass
    def getGameNumber(self):
        return self.gameNum
            
    
           
