import importlib 
from time import time
from os import path, mkdir

class SolutionManager():

    def get_puzzle(self, year, day, input):

        try:
            module_name = f'year_{year}.day_{day}'
            puzzle_module = importlib.import_module(module_name)
        except ModuleNotFoundError:
            exit(f"Puzzle for {year} Day {day} not found. Fucking solve it first dumbass")

        return puzzle_module.Puzzle(input)

    def solve_puzzle(self, year, day, input):
        puzzle = self.get_puzzle(year, day, input)
        part1_sol, part2_sol = puzzle.part1(), puzzle.part2()

        print(f'AOC Day {day} Year {year} Solutions')
        print(f'Part 1 Solution: {part1_sol}')
        print(f'Part 2 Solution: {part2_sol}')


def create_new_year(year):
    folder_name = f'year_{year}'

    try:
         mkdir(folder_name)
    except FileExistsError:
         exit(f"'{folder_name}' already exists.")
    
    puzzle_template = '''
class Puzzle:
    def __init__(self, input):
        pass

    def part1(self):
        pass

    def part2(self):
        pass
    '''
 
    for i in range(1,26):
        filename = f'day_{i}.py'
        if path.exists(filename):
            print(f"'{filename}' already exists. Skipping...")
            continue

        with open(f'{folder_name}/{filename}' ,'w') as f:
            f.write(puzzle_template)

