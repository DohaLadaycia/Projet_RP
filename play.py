from manacalaBoard import MancalaBoard
from game import Game
import math
import copy
from interface import Interface
from random import choice
import time
class Play:
    def  humanTurn(self,game,fosse):
        if fosse in game.state.possibleMoves(game.player):
            side=game.state.doMove(fosse,game.player)
            if side==1:
                game.player=game.player
            else:
                game.player=-game.player
        else:
                print("Vous ne pouvez pas jouer cette fosse!!! ")
               # self.humanTurn(game,fosse)
    def computerTurn(self,game,player):
        k=None
        if player==1:
            p=game.state.player1
        else:
            p=game.state.player2
        for key in p:
            g=copy.deepcopy(game)
            if g.state.doMove(key,player)==1:
                k=key
        if k!=None:
           side=game.state.doMove(k,player)
        else:
          bestValue,fosse=self.MinMaxAlphaBetaPruning(game,player,15,math.inf,-math.inf)
          side=game.state.doMove(fosse,player)
        if side==1:
                game.player=game.player
        else:
             game.player=-game.player
    def MinMaxAlphaBetaPruning (self,game, player, depth, alpha, beta):
      if game.gameOver()==True or depth == 1:
        bestValue = game.evaluate()
        bestPit = None
        return bestValue, bestPit
      if player != game.playerSide:
        bestValue =-math.inf
        for pit in game.state.possibleMoves(player):
            child_game = copy.deepcopy(game)
            if child_game.state.doMove(pit,player)==0:
                value,_ = self.MinMaxAlphaBetaPruning(child_game ,-player,depth-1,alpha, beta)
            else:
                value,_ = self.MinMaxAlphaBetaPruning(child_game ,player,depth-1,alpha, beta)
            if value > bestValue:
                bestValue = value
                bestPit =pit
            alpha = max(alpha, bestValue)
            if beta <= alpha:
                break
        return bestValue,bestPit
      else:
        bestValue =math.inf
        for pit in game.state.possibleMoves(player):
            child_game =copy.deepcopy(game) 
            if child_game.state.doMove(pit,player)==0:
                value,_ = self.MinMaxAlphaBetaPruning(child_game ,-player,depth-1,alpha, beta)
            else:
                value,_ = self.MinMaxAlphaBetaPruning(child_game ,player,depth-1,alpha, beta)
            if value < bestValue:
                bestValue = value
                bestPit =pit
            beta = min(beta, bestValue)
            if beta <= alpha:
                break
        return bestValue,bestPit
dict={'A':4,'B':4,'C':4,'D':4,'E':4,'F':4,'M1':0,'L':4,'K':4,'J':4,'I':4,'H':4,'G':4,'M2':0}
dict={'A':0,'B':0,'C':0,'D':1,'E':0,'F':4,'M1':0,'L':4,'K':4,'J':4,'I':4,'H':4,'G':4,'M2':0}
dict={'A':0,'B':0,'C':0,'D':0,'E':0,'F':4,'M1':0,'L':0,'K':0,'J':0,'I':0,'H':0,'G':4,'M2':0}
intrfece=Interface()
man=MancalaBoard(dict)
menu=True
while menu==True:
  side=intrfece.menu()
  if side==1 or side==-1:
    menu=False
game=Game(man,side)
play=Play()
while (game.gameOver()==False):
    intrfece.draw(dict)
    if(game.player==side):
      a=intrfece.human()
      if (a in dict):
        play.humanTurn(game,a)
    else:
      play.computerTurn(game,-side)
if game.findWinner()==1:
    print('1')
    intrfece.win(1)
    time.sleep(3)
else:
    print('2')
    intrfece.win(2)
    time.sleep(3)
"""H3: Have as many moves as possible from which to choose. This heuristic takes into account
the possible moves that the player might take at each turn and weights the benefits of having more
moves to choose from for each turn. It has a look ahead of one"""