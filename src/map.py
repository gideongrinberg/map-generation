import json
import random

from cell import Cell
from tile import Direction, Tile

""" The "main" class of the program, generates a map. It also contains some other utils for the map. """


class Map:
    map = []  # Initialize the map as an empty array.

    width = 90
    height = 90

    def __init__(self, width=90, height=90):
        self.width = width
        self.height = height

        self._init_map_array()

    def run(self):
        for x in range(len(self.map)):
            for y in range(len(self.map)):  # Loops through every row and colum
                if self.map[x][y] == 0:  # If the cell hasn't been filled
                    try:
                        tile = map[x - 1][y].get_match(
                            self.map[x][y]
                        )  # Create a new game tile based on the adjacency rules.
                        self.map[x][
                            y
                        ] = tile.as_array()  # Convert the tile into an array.
                    except:
                        self.map[x][
                            y
                        ] = (
                            Tile.from_random().as_array()
                        )  # If we can't find a match or we can't find the correct tile, use a random one.
        return self.map

    """ Populates map array with empty values, then places down the first tile. """

    def _init_map_array(self):
        possible_combos = Tile.possible_tiles()

        for x in range(0, self.width):
            self.map.append([])

            for y in range(0, self.height):
                self.map[x].append(0)

        self.map[0][0] = random.choice(
            possible_combos
        )  # Place down a random first tile.
