""" Exercise robot simulator from exercism.
https://exercism.org/tracks/python/exercises/robot-simulator"""

EAST = 0
NORTH = 1
WEST = 2
SOUTH = 3


class Robot:
    """Move the robot from the starting position to the end position and give some instructions.
    It is assumed that the robot is orientated to the north in the starting position,
    so a turn to the east/west or a forward movement is carried out first."""

    def __init__(self, direction=NORTH, x_pos: int = 0, y_pos: int = 0):
        """method that specifies the initial position of the robot on the abscissa
        and ordinate axis, with north as the initial direction.

        Parameters
        --------
        direction: NORTH
        x_pos: int
        y_pos: int
        """
        self.coordinates = (x_pos, y_pos)
        self.direction = direction

    def moveRight(self):
        """Method that allow the robot to turn right in direction,
        following a different direction."""
        self.direction = (self.direction - 1) % 4

    def moveLeft(self):
        """Method that allow the robot to turn left in direction,
        following a different direction."""
        self.direction = (self.direction + 1) % 4

    def advance(self):
        """Method that allow the robot to move forward,
        following a different coordinate, according to its orientation."""
        if self.direction == NORTH:
            self.coordinates = (self.coordinates[0], self.coordinates[1] + 1)
        elif self.direction == SOUTH:
            self.coordinates = (self.coordinates[0], self.coordinates[1] - 1)
        elif self.direction == WEST:
            self.coordinates = (self.coordinates[0] - 1, self.coordinates[1])
        elif self.direction == EAST:
            self.coordinates = (self.coordinates[0] + 1, self.coordinates[1])

    def move(self, instructions: str):
        """Move method where we specify the final position of the robot
        according to the input received (instructions: str) by calling the methods described
        and implemented previously.

        Parameters
        --------
        instructions: str
        """
        for i in instructions:
            if i == "R":
                self.moveRight()
            elif i == "L":
                self.moveLeft()
            elif i == "A":
                self.advance()


'''EAST = "E"
NORTH = "N"
WEST = "W"
SOUTH = "S"

class Robot2:

     """Move the robot from the starting position to the end position and give some instructions. It is assumed that the robot is orientated to the north in the starting position, so a turn to the east/west or a forward movement is carried out first.
    """
    def __init__(self, direction=NORTH, x_pos:int=0, y_pos:int=0):

        self.coordinates = (x_pos,y_pos)
        self.direction = direction

    def moveRight(self):
        
        if self.direction == NORTH:
            self.direction = EAST
        elif self.direction == EAST:
            self.direction = SOUTH
        elif self.direction == SOUTH:
            self.direction = WEST
        elif self.direction == WEST:
            self.direction = NORTH

        self.direction = (self.direction - 1) % 4
            
    def moveLeft(self):
        
        if self.direction == NORTH:
            self.direction = WEST
        elif self.direction == WEST:
            self.direction = SOUTH
        elif self.direction == SOUTH:
            self.direction = EAST
        elif self.direction == EAST:
            self.direction = NORTH

    
    def advance(self):
        
        if self.direction == NORTH:
            self.coordinates = (self.coordinates[0],self.coordinates[1] + 1)
        elif self.direction == SOUTH:
            self.coordinates = (self.coordinates[0],self.coordinates[1] - 1)
        elif self.direction == WEST:
            self.coordinates = (self.coordinates[0] - 1,self.coordinates[1])
        elif self.direction == EAST:
            self.coordinates = (self.coordinates[0] + 1,self.coordinates[1])

    def move(self,instructions):

        for i in instructions:
            if i == "R":
                self.moveRight()
            elif i == "L":
                self.moveLeft()
            elif i == "A":
                self.advance()'''
