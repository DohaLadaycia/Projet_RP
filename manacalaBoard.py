class MancalaBoard:
    def __init__(self,board):
        self.board=board
        self.player1=('A','B','C','D','E','F')
        self.player2=('G','H','I','J','K','L')
        self.obbesse={'A':'G','B':'H','C':'I','D':'J','E':'K','F':'L','G':'A','H':'B','I':'C','J':'D','K':'E','L':'F'}
        self.suivant={'A':'B','B':'C','C':'D','D':'E','E':'F','F':'M1','M1':'L','L':'K','K':'J','J':'I','I':'H','H':'G','G':'M2','M2':'A'}
    def possibleMoves(self,player):
        fosses=[]
        player=self.player1 if player==1 else self.player2 
        for key in player:
            if self.board[key]!=0:
                fosses.append(key)
        return fosses
    def doMove(self,fosse,player):
        fosse1=fosse
        while self.board[fosse]>0:
            if ((self.suivant[fosse1]=='M1' and player==-1) or(self.suivant[fosse1]=='M2' and player==1)):
                fosse1=self.suivant[fosse1]
            else:
                self.board[self.suivant[fosse1]]=self.board[self.suivant[fosse1]]+1
                fosse1=self.suivant[fosse1]
                self.board[fosse]=self.board[fosse]-1
        if (self.board[fosse1]==1 and ((fosse1 in self.player1 and player==1)or(fosse1 in self.player2 and player==-1))):
            if player==1:
                self.board[fosse1]=self.board[fosse1]-1
                self.board['M1']=self.board['M1']+self.board[self.obbesse[fosse1]]+1
                self.board[self.obbesse[fosse1]]=0
            else:
                self.board[fosse1]=self.board[fosse1]-1
                self.board['M2']=self.board['M2']+self.board[self.obbesse[fosse1]]+1
                self.board[self.obbesse[fosse1]]=0
        #print(self.board)
        if ((fosse1=='M1' and player==1) or(fosse1=='M2' and player==-1)):
            return 1
        else:
            return 0




