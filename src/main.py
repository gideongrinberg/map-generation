""" A procedural map generator in Python, based on ARENA (Bhojan et. al. 2014) and Wang Tiles. """

import argparse

from map import Map

parser = argparse.ArgumentParser()

parser.add_argument("width", help="The width of the output. Required", type=int)
parser.add_argument("height", help="The height of the output. Required.", type=int)

args = parser.parse_args()

map = Map(args.width, args.height)
map = map.run()

print(map)
