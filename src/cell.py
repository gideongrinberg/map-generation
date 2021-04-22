import random
from enum import Enum

class Cell(Enum):
    """ An enum of cell types. """
    Outdoor = 0
    Indoor = 1
    Wall = 2

    """ Gets a random cell type. """
    @staticmethod
    def random_cell():
        return random.choice([Cell.Indoor, Cell.Outdoor, Cell.Wall])
    
    """ Converts a cell to a character. """
    @staticmethod
    def to_char(cell):
        if cell == Cell.Indoor:
            return "I"
        elif cell == Cell.Outdoor:
            return "O"
        elif cell == Cell.Wall:
            return "W"