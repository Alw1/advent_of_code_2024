from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("source")

args = parser.parse_args()

with open(args.source, 'r') as f:
    reports = [[*map(int, line.split())] for line in f.readlines()]

def is_safe(level):
    level_diff = [(x-y) for x,y in zip(level[0::], level[1::])]

    neg = len(list(filter(lambda x: x < 0, level_diff)))
    pos = len(list(filter(lambda x: x > 0, level_diff))) 

    prob_dampener = True
    for diff in level_diff:
        if not (1 <= diff <= 3):
            if not prob_dampener:
                return False
            else:
                prob_dampener = False

        print(report,neg,pos,diff, ' is safe')
    if abs(neg-pos) != len(level_diff):
        return False

    return True


safe = 0
for report in reports:
    safe += is_safe(report)

print(f'{safe} safe reports')


