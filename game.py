from manacalaBoard import MancalaBoard
class Game:
    def __init__(self,manacalaBoard,playerSide):
        self.state=manacalaBoard
        self.player=1
        self.playerSide=playerSide
    def  gameOver(self):
        finie=True
        for key in (self.state.player1):
            if self.state.board[key]!=0:
                finie=False
        if finie==True:
            for key in (self.state.player2):
                self.state.board['M2']=self.state.board['M2']+self.state.board[key]
                self.state.board[key]=0
        else:
          finie=True
          for key in (self.state.player2):
            if self.state.board[key]!=0:
                finie=False
          if finie==True:
            for key in (self.state.player1):
                self.state.board['M1']=self.state.board['M1']+self.state.board[key]
        return finie
    def  findWinner(self):
        if(self.state.board['M1']>self.state.board['M2']):
            return (1)
        else:
            return (2)
    def evaluate(self):
        vide=0
        vide_opp=0
        if self.playerSide==1:
            p=self.state.player1
        else:
            p=self.state.player2
        for k in self.state.board:
            if (k in p and self.state.board[k]==0 and k!='M1'and k!='M2'):
                vide=vide+1
            elif (k not in p and self.state.board[k]==0 and k!='M1'and k!='M2'):
                vide_opp=vide_opp+1
        v=vide-vide_opp
        if self.playerSide==1:
            return 3*(self.state.board['M2']-self.state.board['M1'])+v
        else:
            return 3*(self.state.board['M1']-self.state.board['M2'])+v

