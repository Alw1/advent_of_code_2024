from argparse import ArgumentParser
from re import findall,search

parser = ArgumentParser()
parser.add_argument("source")

args = parser.parse_args()

with open(args.source, 'r') as f:
    mul_instr_regex = r"mul\((\d+),(\d+)\)"
    do_regex = r"(do\(\))" 
    dont_regex = r"(don't\(\))"
    
    part2_regex = do_regex + '|' + dont_regex + '|' + mul_instr_regex

    text = f.read()
    instructions = findall(mul_instr_regex, text)
    part2_instructions = findall(part2_regex, text)

    enabled = True

    sum = 0
    for w,x,y,z in part2_instructions:
        if w == 'do()':
            enabled = True
        if x == 'don\'t()':
            enabled = False

        if enabled and (y != '' and z != '1'):
            sum += int(y) * int(z)

    print(f'Solution: {sum}')


