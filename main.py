from argparse import ArgumentParser
from utils import SolutionManager, create_new_year
import os.path

parser = ArgumentParser(description="My Advent of Code Solution Archive")
parser.add_argument('-y', '--year', help="Year of solution")
parser.add_argument('-d', '--day', help="Day of solution")
parser.add_argument('-f', '--file', help="File containing input data")
parser.add_argument('-c', '--create_new_year', type=int, help="Create folder and templates for a new year")

args = parser.parse_args()

aoc_session = '53616c7465645f5fdce926d9642bd6788e9aba0eb56e5c0f47e7b3da5bfc8949f138b34367d7d167641567de8ea935f07fe56fabfe4d595683b35871ca8813e5'

if __name__ == '__main__':
    
    if args.create_new_year is not None:
        create_new_year(args.create_new_year)
        exit()

    with open(args.file, 'r') as f:
        input = [line.strip() for line in f.readlines()]

    sol_manager = SolutionManager()
    sol_manager.solve_puzzle(args.year, args.day, input)
