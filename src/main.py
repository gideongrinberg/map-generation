""" A procedural map generator in Python, based on ARENA (Bhojan et. al. 2014) and Wang Tiles. """

import argparse
import random

from tile import Tile, Direction
from cell import Cell

parser = argparse.ArgumentParser()

parser.add_argument("width", help = "The width of the output. Required", type = int)
parser.add_argument("height", help = "The height of the output. Required.", type = int)

args = parser.parse_args()
possible_combos = Tile.possible_tiles()

map = []

# # ? Prefills array. Is this needed?
for x in range(0, args.width):
    map.append([])

    for y in range(0, args.height):
        map[x].append(0)

map[0][0] = random.choice(possible_combos)

for x in range(len(map)):
    for y in range(len(map)):
        if map[x][y] == 0: # If map is an empty cell
            try:
                map[x][y] = map[x-1][y].get_match(map[x][y])
            except:
                map[x][y] = Tile.from_random()

map_to_str(map)

def map_to_str(map):
    for map_x in range(len(map)):
        for map_y in range(len(map)):
            for cell_x in range(len(map[map_x][map_y].tiles)):
                for cell_y in range(len(map[x][y].tiles[cell_x])):
                    print(map[x][y].tiles[map_x][map_y].__str__())


