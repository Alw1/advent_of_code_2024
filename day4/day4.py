from argparse import ArgumentParser
from re import findall,search

parser = ArgumentParser()
parser.add_argument("source")

args = parser.parse_args()

with open(args.source, 'r') as f:
    lines = [*map(lambda x: x.strip(), f.readlines())]


def count_xmas(lines):
    ''' Counts how many times XMAS occurs in a text
        including diagonally and backwards
    '''
    
    for line in lines:
        for i in range(len(line)-1):

    pass


