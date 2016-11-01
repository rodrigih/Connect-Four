'''
 This python test is a unit test of testing the moves in
 the connect four, which includes:
   - dropping a piece
   - popping a piece from a column
   - special case of droping a piece to a full column
   - special case of popping a piece from an empty column
   - passing incorrect typed arguments (anything other than an int)
   - passing non-sensical arguments (out of bound numbers)
'''
   
import unittest
import connectFour as CF

class TestMovesMethods(unittest.TestCase):

    def setUp(self):
        self.Board = CF.GameBoard()

    def test_dropping_piece_in_each_column(self):
        for i in range(self.Board.columns):
            self.Board.drop(i)
            self.assertNotEqual(self.Board[i][self.Board.rows-1],"-")

    def test_dropping_piece_until_column_full(self):
        rows = self.Board.rows - 1
        for i in range(self.Board.rows):
            self.Board.drop(0)
            self.assertNotEqual(self.Board[0][rows-i],"-")

    def test_dropping_piece_in_full_column(self):
        for i in range(self.Board.rows):
            self.Board.drop(0)
        with self.assertRaises(CF.InvalidMoveError):
            self.Board.drop(0)

    def test_dropping_piece_in_out_of_range_column(self):
        with self.assertRaises(CF.InvalidMoveError):
            self.Board.drop(-1)

        with self.assertRaises(CF.InvalidMoveError):
            self.Board.drop(self.Board.rows+1)

    def test_popping_column(self):
        self.Board.drop(0)
        self.assertNotEqual(self.Board[0][-1],"-")
        self.Board.pop(0)
        self.assertEqual(self.Board[0][-1],"-")

    def test_popping__empty_column(self):
        with self.assertRaises(CF.InvalidMoveError):
            self.Board.pop(0)

    def test_popping_out_of_range_column(self):
        with self.assertRaises(CF.InvalidMoveError):
            self.Board.pop(-1)
        with self.assertRaises(CF.InvalidMoveError):
            self.Board.pop(self.Board.rows+1)

if __name__ == '__main__':
    unittest.main()
