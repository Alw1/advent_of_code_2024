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

sum_tuple = lambda x: abs(x[1] - x[0])

distance = 0
for x in s:
    distance += sum_tuple(x)

similarity_score = 0

for num in l1:
    similarity_score += num * l2.count(num)

#distance = functools.reduce(lambda x,y: sum_tuple(x) + sum_tuple(y), list(zip(l1,l2)) )
    
print(f'The distance is {distance}')
print(f'The similarity score is {similarity_score}')






