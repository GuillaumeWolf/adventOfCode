import numpy as np

# input
list1 = []
list2 = []
with open("input.txt", "r") as file:
    for line in file:
        vals = line.strip().split()
        list1.append(int(vals[0]))
        list2.append(int(vals[1]))

# check equal length
if not len(list1)==len(list2):
    print('Lengths of the two lists are differents. ')



# Resolve Part 1
def part1(list1, list2):
    d = 0
    while len(list1)>0:
        d += abs(min(list1) - min(list2))
        list1.remove(min(list1))
        list2.remove(min(list2))

    print('Part 1:', d)


# Resolve Part 2
def part2(list1, list2):
    d = 0
    for x in list1:
        d += x * list2.count(x)

    print('Part 2:', d)



part2(list1, list2)
part1(list1, list2)

