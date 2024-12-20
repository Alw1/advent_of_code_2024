class Puzzle:
    
    def __init__(self, input):
        l1,l2 = [],[]
        for line in input:
            x,y = line.split()
            l1.append(int(x))
            l2.append(int(y))

        l1.sort()
        l2.sort()

        self.l1, self.l2 = l1, l2

    def part1(self):
        return sum([abs(x[1] - x[0]) for x in zip(self.l1, self.l2)])

    def part2(self):
        return sum([x * self.l2.count(x) for x in self.l1])
    






