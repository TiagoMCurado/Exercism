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

        
        pass
        # self.row e self.column e ver se estao dentro dos valores possiveis, de 0 a 7 ou 1 a 8, conforme estruturado

    def can_attack(self, another_queen):
        # receber outro objecto. fazer another_queen.row ou another_queen.column
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Invalid queen position: both queens in the same square")
        else:
            if self.row == another_queen.row or self.column == another_queen.column:
                return True
            elif abs(self.row - another_queen.row) == abs(self.column - another_queen.column):
                 return True
            else:
                return False

        pass
