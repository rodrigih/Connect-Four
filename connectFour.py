from random import choice as randomPick

class InvalidMoveException:
    pass

class GameBoard:
    '''
    This class is used to represent the game of connect four.

    It contains the following class variables:
        rows: the number of rows in the board. Defaults to 6
        columns: the number of columns in the board. Defaults to 7
        board: the 2-d array used to represent the board
        turn: the player of whom the current turn belongs to
        header: the string numbering the columns. Used when printing the board
                onto the console
    '''

    def __init__(self):
        self.rows = 6
        self.columns = 7
        self.board = self._createBoard()
        self.turn = randomPick(["R","Y"])
        self.header = self._createHeader()

    def __str__(self):
        s = "\n".join([" ".join([column[i] for column in self.board]) for i in range(self.rows)])
        return "\n%s\n%s\n" % (self.header,s)

    ## Helper Functions

    def _createBoard(self):
        return [['-' for i in range(self.rows)] for j in range(self.columns)]
    
    def _createHeader(self):
        return " ".join([str(i+1) for i in range(self.columns)])

    def _findEmptySlot(self,column):
        '''
        Given a column, gives the lowest empty slot
        '''
        index = 0

        for slot in self.board[column]:
            if(slot != '-'):
                break
            index += 1

        # Column is filled, so raise error
        if(index == 0):
            raise Exception

        # index is first filled slot, so return index minus 1
        return index - 1

    # The following helper functions check if there is four
    # consecutive pieces in the specified directions.

    def _checkVerticalTop(self):
        pass

    def _checkVerticalBottom(self):
        pass

    def _checkHorizontalLeft(self):
        pass

    def _checkHorizontalRight(self):
        pass

    ## Class Methods

    def clearBoard(self):
        self.board = self._createBoard()

    def switchPlayer(self):
        if (self.turn == "R"):
            self.turn = "Y"
        else:
            self.turn = "R"

    def getCurrentPlayer(self):
        return self.turn

    def dropPiece(self,column):
        '''
        Drops a piece at the specified column
        '''
        row = self._findEmptySlot(column)
        self.board[column][row] = self.turn
        # self.checkWinner() # <- add when implemented
        self.switchPlayer()

    def popColumn(self,column):
        '''
        Pops the bottom-most piece of the specified column
        '''
        self.board[column] = ['-'] + self.board[column][:-1]
        # self.checkWinner # <- add when implemented
        self.switchPlayer()

    def checkWinner(self,row,column,move):
        '''
        Checks the board to see if there is any winner.
        '''
        pass

    ## Overloaded Class Methods
    def __eq__(self,other):
        '''
        Two boards are considered equal if they have the
        same pieces in the same place. The current player
        is irrelevant.
        '''
        if isinstance(other, self.__class__):
            return self.board == other.board
        return NotImplemented

    def __ne__(self,other):
        if isinstance(other,self.__class__):
            return not self.__eq__(other)
        return NotImplemented

def main():
    board = GameBoard();
    print(board)

    print("\nTesting\n")
    testHeader = "\n" + " ".join([str(i+1) for i in range(board.columns)])
    testString = (" ".join(["-" for i in range(board.columns)]) + "\n") * board.rows
    print(testHeader + "\n" + testString)
main()
