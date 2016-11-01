'''
This python file is a test suite for checking a winner in connect four.
It includes cases where the winning 4 pieces are:
    - horizontal
    - diagonal
    - vertical
    - horizontal and diagonal caused by popping a piece from the bottom

It also includes the case where popping a column causes 2 'winners'
(in this case, the player that committed the 'pop' move is the actual
winner).
'''

import unittest
import connectFour as CF

class TestCheckingForWinner(unittest.TestCase):

    def setUp(self):
        self.Board = CF.GameBoard()

    def test_horizontal_winner(self):
        # Moves were choses so that winner is player to move first
        winner = self.Board.turn
        col = 0
        for i in range(8):
            if(i % 2 == 0):
                self.Board.drop(col)
                col += 1
            else:
                self.Board.drop(0)
        self.assertEqual(self.Board.winner,winner)

    def test_vertical_winner(self):
        # Moves were choses so that winner is player to move first
        winner = self.Board.turn
        for i in range(8):
            if(i % 2 == 0):
                self.Board.drop(0)
            else:
                self.Board.drop(1)
        self.assertEqual(self.Board.winner,winner)
    
    def test_diagonal_winner(self):
        # Moves were choses so that winner is player to move first
        winner = self.Board.turn
        moves = [0,1,1,2,3,2,2,3,3,4,3]
        for i in moves:
            self.Board.drop(i) 
        self.assertEqual(self.Board.winner,winner)


    def test_horizontal_winner_caused_by_pop(self):
        # Moves were choses so that winner is player to move second
        loser = self.Board.turn
        moves = [0,1,1,0,2,2,5,3,6,4,0] # These moves will be "drop"
        winningMove = 2 # This move will be "pop"

        for i in moves:
            self.Board.drop(i)
        self.Board.pop(winningMove)

        # Check winner is not 'None' or 'loser' (player who moved first)
        self.assertNotEqual(self.Board.winner,None)
        self.assertNotEqual(self.Board.winner,loser)
    
    def test_diagonal_winner_caused_by_pop(self):
        # Moves were choses so that winner is player to move first
        winner = self.Board.turn
        moves = [0,1,1,2,3,2,2,3,3,3,3] # These moves will be "drop"
        winningMove = 3 # These moves will be "pop"

        for i in moves:
            self.Board.drop(i) 
        self.Board.pop(winningMove)

        self.assertEqual(self.Board.winner,winner)

    def test_pop_causing_two_winners(self):
        # Moves were choses so that winner is player to move second
        loser = self.Board.turn
        moves = [3,3,3,2,2,1,1,4,4,5,5] # These moves will be "drop"
        winningMove = 3 # These moves will be "pop"

        for i in moves:
            self.Board.drop(i)

        self.Board.pop(winningMove)

        self.assertNotEqual(self.Board.winner,None)
        self.assertNotEqual(self.Board.winner,loser)

if __name__ == "__main__":
    unittest.main()
