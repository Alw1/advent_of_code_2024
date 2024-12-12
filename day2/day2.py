from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("source")

args = parser.parse_args()

with open(args.source, 'r') as f:
    reports = [[*map(int, line.split())] for line in f.readlines()]

def is_safe(level):
    level_diff = [(x-y) for x,y in zip(level[0::], level[1::])]
    pos, neg = 0,0
    prob_dampener = False
    for diff in level_diff:
        if not (1 <= abs(diff) <= 3):
            if prob_dampener:
                return False
            else:
                prob_dampener = True
        
        if diff > 0:
            pos += 1
        else:
            neg += 1

    if (pos - len(level)-1 <= 1) or (neg - len(level-1)-1 <= 1) and (prob_dampener == False):
        if prob_dampener:
            return True
        return False
    else:
        return False


safe = 0
for report in reports:
    safe += is_safe(report)
#    print(report)

print(f'{safe} safe reports')


