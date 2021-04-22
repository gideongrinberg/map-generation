"""Implementation for GameTiles, and various utilites surrounding it."""

import random
import numpy as np

from typing import List
from itertools import product
from enum import Enum

from cell import Cell

class Direction(Enum):
    """ An enum of positions. Name is a misnomer."""
    TOP_LEFT = 0
    TOP_RIGHT = 1
    BOTTOM_LEFT = 2
    BOTTOM_RIGHT = 3

class Tile:
    """A basic tile class used in map generation."""

    tiles = []
    initialized = False

    def __init__(self):
        super().__init__()
    
    """ Get a cell at a specific position.
    
    Args:
        position (Direction): The position of the cell to get.

    Returns:
        Cell: The cell at the specified position.
    
    Raises:
        ValueError: If position isn't a valid position.
    """
    def get_cell(self, position):
        if position == Direction.TOP_LEFT:
            return self.tiles[0][0]
        elif position == Direction.TOP_RIGHT:
            return self.tiles[0][1]
        elif position == Direction.BOTTOM_LEFT:
            return self.tiles[1][0]
        elif position == Direction.BOTTOM_RIGHT:
            return self.tiles[1][1]
        else:
            raise ValueError("Invalid argument for position.")
    
    """Checks if two cells match according to the 'Rules of Adjacency'. See Bhojan, Wong (2014) for details.
    
    Args:
        match (Tile): The tile to check against.
        side (int): Which edge to match against. Zero for left, one for right (zero will check the left side of the tile against `match`'s right, one will check the right side against `match`'s left.)
    Returns:
        bool: True if the tiles match according to the Rules of Adjacency, false if they don't.
    Raises:
        ValueError: Raised if side is not 0 or 1.
    """
    def is_match(self, match, side: int = 0):
        if side == 0:
            if self.get_cell(Direction.TOP_LEFT) == match.get_cell(Direction.TOP_RIGHT) and self.get_cell(Direction.BOTTOM_LEFT) == match.get_cell(Direction.BOTTOM_RIGHT):
                return True
            else:
                return False 
        elif side == 1:
            if self.get_cell(Direction.TOP_RIGHT) == match.get_cell(Direction.TOP_LEFT) and self.get_cell(Direction.BOTTOM_RIGHT) == match.get_cell(Direction.BOTTOM_LEFT):
                return True
            else:
                return False 
        else:
            raise ValueError(f"Parameter `side` of Tile.is_match should be 0 or 1, not {side}")

    def find_match(self, side=0):
        if side == 0:
            top_right = self.get_cell(Direction.TOP_LEFT)
            top_left = Cell.random_cell()

            bottom_right = self.get_cell(Direction.BOTTOM_LEFT)
            bottom_left = Cell.random_cell()

            retVal = Tile.from_cells(top_left, top_right, bottom_left, bottom_right)
            assert(self.is_match(retVal, side = side))

            return retVal

    """Creates a new Tile from the specified cells.
    Args:
        left_t (Cell): The top left cell (`tile.tiles[0][0]` or `tile.get_cell(directions.TOP_LEFT)`)
        right_t (Cell): The top right cell (`tile.tiles[0][1]` or `tile.get_cell(directions.TOP_RIGHT)`)
        left_b (Cell): The bottom left cell (`tile.tiles[1][0]` or `tile.get_cell(directions.BOTTOM_LEFT)`)
        right_b (Cell): The top left cell (`tile.tiles[1][1]` or `tile.get_cell(directions.BOTTOM_RIGHT)`)
    Returns:
        Cell: The new `Tile`.
    Examples:
        >>> my_tile = Tile.from_cells(Cell.Outdoors, Cell.Indoors, Cell.Wall, Cell.Wall)
        >>> print(my_tile.__str__(pretty_print=True))
        O I
        W W
    """
    @staticmethod
    def from_cells(left_t: Cell, right_t: Cell, left_b: Cell, right_b: Cell):
        retVal = Tile()

        retVal.tiles = [[left_t, right_t], [left_b, right_b]]
        retVal.initialized = True

        return retVal
    
    """Creates a new tile from the specified array of cells.
    Args:
        input: The 2D array to use as input. Input cannot be a jagged array, and should be a Python list (not a NumPy array.)
    Returns:
        Tile: The new tile.
    """
    @staticmethod
    def from_2d_array(input):
        retVal = Tile()

        retVal.tiles = input
        retVal.initialized = True

        return retVal
    
    """Creates a new tile from the specified array of cells.
    Args:
        input: The 1D array to use as input. Should be of length 4.
    Returns:
        Tile: The new tile.
    """
    @staticmethod
    def from_array(input):
        assert(len(input) == 4)
        retVal = Tile()

        retVal.tiles = [[input[0], input[1]], [input[2], input[3]]]
        retVal.initialized = True

        return retVal
    
    """Creates a new tile with `cells` populated randomly.
    Returns:
        Tile: The new tile.
    """
    @staticmethod
    def from_random():
        retVal = Tile()

        retVal.tiles = [[Cell.random_cell(), Cell.random_cell()], [Cell.random_cell(), Cell.random_cell()]]
        retVal.initialized = True

        return retVal
    
    """ Gets every possible valid tile.
    Returns:
        List[Tile]: A list of valid tiles.
    """
    @staticmethod
    def possible_tiles():
        combos = product(list(Cell), repeat=4)

        retVal = []
        for combo in combos:
            retVal.append(Tile.from_array(list(combo)))
                
        return retVal

    """Returns a string representation of the Tile.
    Args:
        pretty_print (bool): If True, the return value will be formatted using whitespace, without brackets. Default: true.
    Returns:
        str: A string representation of the tile.
    """
    def __str__(self, pretty_print: bool = True):
        if pretty_print:
            return f"{Cell.to_char(self.tiles[0][0])} {Cell.to_char(self.tiles[0][1])}\n{Cell.to_char(self.tiles[1][0])} {Cell.to_char(self.tiles[1][1])}"
        else:
            return self.tiles.__str__()

