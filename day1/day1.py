import functools
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("source")

args = parser.parse_args()

with open(args.source, 'r') as f:
    lines = f.readlines()

l1, l2, = [], []

for line in lines:
    x,y = line.split()
    l1.append(int(x))
    l2.append(int(y))

l1.sort()
l2.sort()

s = list(zip(l1,l2))

distance = sum([abs(x[1] - x[0]) for x in s])
similarity_score = sum([x * l2.count(x) for x in l1])
    
print(f'The distance is {distance}')
print(f'The similarity score is {similarity_score}')






