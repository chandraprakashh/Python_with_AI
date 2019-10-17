# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 22:50:57 2019

@author: user
"""


# Code => 1
from easyAI import TwoPlayersGame, Human_Player, AI_Player, Negamax

class GameOfBones( TwoPlayersGame ):

    def __init__(self, players):
        self.players = players
        self.pile = 20 
        self.nplayer = 1 

    def possible_moves(self): return ['1','2','3']
    def make_move(self,move): self.pile -= int(move) 
    def win(self): return self.pile<=0 
    def is_over(self): return self.win() 
    def show(self): print ("%d bones left in the pile" % self.pile)
    def scoring(self): return 100 if game.win() else 0 

ai = Negamax(13) 
game = GameOfBones( [ Human_Player(), AI_Player(ai) ] )
history = game.play()




# Code => 2
from easyAI import TwoPlayersGame, AI_Player, Negamax 
from easyAI.Player import Human_Player 

class GameController(TwoPlayersGame): 
    def __init__(self, players): 
        self.players = players 
        self.nplayer = 1  
        self.board = [0] * 9 

    def possible_moves(self): 
        return [a + 1 for a, b in enumerate(self.board) if b == 0] 

    def make_move(self, move): 
        self.board[int(move) - 1] = self.nplayer 

    def loss_condition(self): 
        possible_combinations = [[1,2,3], [4,5,6], [7,8,9], 
            [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]] 
        return any([all([(self.board[i-1] == self.nopponent) 
               for i in combination]) for combination in possible_combinations])  

    def is_over(self): 
        return (self.possible_moves() == []) or self.loss_condition() 

    def show(self): 
        print('\n'+'\n'.join([' '.join([['. ', 'O', 'X'][self.board[3*j + i]] 
                for i in range(3)]) for j in range(3)])) 

    def scoring(self): 
        return -100 if self.loss_condition() else 0 

if __name__ == "__main__": 
    algorithm = Negamax(7) 

    GameController([Human_Player(), AI_Player(algorithm)]).play() 

