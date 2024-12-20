from argparse import ArgumentParser
from random import shuffle

parser = ArgumentParser()
parser.add_argument("source")

args = parser.parse_args()

with open(args.source, 'r') as f:
    lines = [line.strip() for line in f.readlines()]

page_order_rules = []
page_numbers = []

for i,line in enumerate(lines):
    if line.strip() == '':
        page_order_rules = [y.split('|') for y in lines[:i]]
        page_numbers = [y.split(',') for y in lines[i+1:]]
        break

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
            temp = update
            temp[page1_idx] = y
            temp[page2_idx] = x
            fucked_up_updates.append(temp)
            break
    else:
        middle_num_sum += int(update[len(update) // 2])

#def reorder(rules, updates):
#   while True:
#        ordered = True
#        for update in updates:
#            for x,y in rules:
#                try:
#                    page1_idx = update.index(x) 
#                    page2_idx = update.index(y) 
#                except ValueError:
#                    continue
#
#                if page1_idx > page2_idx:
#                    ordered = False
#                    shuffle(update)
#                    break
#        if ordered:
#            return updates

#page_numbers = [[int(x) for x in y.split(',')] for y in page_numbers]
def reorder(rules, updates):
    temp = updates
    for x,y in rules:
        while True:
           for i,update in enumerate(temp):
                ordered = False
                try:
                    page1_idx = update.index(x) 
                    page2_idx = update.index(y) 
                except ValueError:
                    continue

                if page1_idx > page2_idx:
                    ordered = True
                    update[page1_idx] = x
                    update[page2_idx] = y
                    break
        if not ordered:
            temp.append(updates)
            break
        return temp

part2_middle_num_sum = sum([int(update[len(update) // 2]) for update in reorder(page_order_rules,fucked_up_updates)])
print(reorder_update(page_order_rules,fucked_up_updates))

print(middle_num_sum)
print(part2_middle_num_sum)
