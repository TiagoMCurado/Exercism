#https://exercism.org/tracks/python/exercises/queen-attack/

class Queen:
    def __init__(self, row, column):

        self.row = row
        self.column = column
        
        if self.row < 0:
            raise ValueError("row not positive")

        if self.row > 7:
            raise ValueError("row not on board")

        if self.column < 0:
            raise ValueError("column not positive")

        if self.column > 7:
            raise ValueError("column not on board")

    def can_attack(self, another_queen):
        """Possibility of queens attack"""
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Invalid queen position: both queens in the same square")
        #Verification of queens position by row and column
        if self.row == another_queen.row or self.column == another_queen.column:
            return True
        #Verification of queens position by diagonal point of view
        elif abs(self.row - another_queen.row) == abs(self.column - another_queen.column):
            return True
        else:
            return False
