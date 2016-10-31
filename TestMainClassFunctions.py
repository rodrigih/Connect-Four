'''
 This python file is a unit test of the main class functions,
 which includes the following:
   - creating a board
   - printing out the board
   - clearing a board
'''

import unittest
import connectFour as CF

class TestMainClassFunctions(unittest.TestCase):

    def setUp(self):
        self.Board = CF.GameBoard()

    def test_board_creation(self):
        self.assertIsInstance(self.Board,CF.GameBoard,"Did not create object of class 'GameBoard'");
        self.assertEqual(self.Board.columns,len(self.Board.board))
        self.assertEqual(self.Board.rows,len(self.Board.board[0]))

    def test_type_of_class_variables(self):
        self.assertIs(type(self.Board.rows),int)
        self.assertIs(type(self.Board.columns),int)
        self.assertIs(type(self.Board.turn),str)
        self.assertIs(type(self.Board.header),str)

    def test_str_function(self):
       testHeader = "\n" + " ".join([str(i+1) for i in range(self.Board.columns)])
       testRow = " ".join(["-" for i in range(self.Board.columns)]) + "\n"
       testString = testRow * self.Board.rows
       self.assertEqual(self.Board.__str__(),testHeader + "\n" + testString)

    def test_clear_board(self):
        newBoard = CF.GameBoard()
        self.Board.clearBoard();
        self.assertEqual(newBoard,self.Board)
        

if __name__ == '__main__':
    unittest.main()
