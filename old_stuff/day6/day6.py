from argparse import ArgumentParser
from enum import Enum
from random import shuffle

parser = ArgumentParser()
parser.add_argument("source")

args = parser.parse_args()

class Direction(Enum):
    UP = '^'
    DOWN = 'v'
    LEFT = '<'
    RIGHT = '>'

with open(args.source, 'r') as f:
    lines = [line.strip() for line in f.readlines()]

for i,line in enumerate(lines):
    guard_pos = line.find('^')
    
    if guard_pos != -1:
        guard_pos = (guard_pos, i)
        break


print(guard_pos)

