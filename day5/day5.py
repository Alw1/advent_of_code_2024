from argparse import ArgumentParser
from re import findall,search

parser = ArgumentParser()
parser.add_argument("source")

args = parser.parse_args()

with open(args.source, 'r') as f:
    lines = [line.strip() for line in f.readlines()]

page_order_rules = []
page_numbers = []

for i,line in enumerate(lines):
    if line.strip() == '':
        page_order_rules = lines[:i]
        page_numbers = lines[i+1:]
        break

page_order_rules = [[int(x) for x in y.split('|')] for y in page_order_rules]
page_numbers = [[int(x) for x in y.split(',')] for y in page_numbers]
middle_num_sum = 0
part2_middle_num_sum = 0
fucked_up_updates = []

for i, update in enumerate(page_numbers): 
    for x,y in page_order_rules:
        try:
            page1_idx = update.index(x) 
            page2_idx = update.index(y) 
        except ValueError:
            continue

        if page1_idx > page2_idx:
            fucked_up_updates.append(update)
            break
    else:
        middle_num_sum += update[len(update) // 2]


print(fucked_up_updates)
for update in fucked_up_updates:
    for x,y in page_order_rules:
        try:
            page1_idx = update.index(x) 
            page2_idx = update.index(y) 
        except ValueError:
            continue

        if page1_idx > page2_idx:
            update[page1_idx] = y 
            update[page2_idx] = x
            break
    else:
        middle_num_sum += update[len(update) // 2]

part2_middle_num_sum = sum([update[len(update)//2] for update in fucked_up_updates])

print(middle_num_sum)
print(part2_middle_num_sum)
print(fucked_up_updates)
