class GameDetails:
    global firstPlayer
    global secondPlayer
    global gameId

    def __init__(self,gameNum,username):
        self.gameId=gameNum
        self.firstPlayer=username