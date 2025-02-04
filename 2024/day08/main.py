import numpy as np
import awkward as ak
from itertools import permutations, combinations



data = []
with open('input.txt', 'r') as file:
    for line in file:
        data.append([char for char in line.strip()])
data = np.array(data)

city = []
border = data.shape
for i in range(border[0]):
    for j in range(border[1]):
        city.append({'pos': np.array((i,j)), 'f': data[i][j]})


city = ak.Array(city)
frequencies = set(city[city['f']!='.']['f'])
antenna = {frequency: city[city['f']==frequency] 
                for frequency in frequencies}


# print(f'{border = }')
# print(f'{city = }')
# print(f'{frequencies = }')
# print(f'{antenna = }')
# print('_____________\n\n\n')


def is_inside(pos, border):
    cond1 = np.all(pos>=0, axis=1)
    cond2 = np.all(pos<border, axis=1)
    result = np.all((cond1, cond2), axis=0)
    return result


def comput_antinodes(p1,p2,part):
    antinodes = []
    dp = p2-p1
    if part==1:
        antinodes = (p1-dp, p2+dp)
    if part==2:
        for k in (-1,1):
            i=0
            while is_inside(np.array([p1+i*k*dp]), border):
                antinodes.append(p1+i*k*dp)
                i += 1
    return antinodes


def find_antinodes(positions, part):
    antinodes = []
    for p1,p2 in combinations(positions, 2):
        antinodes.append(comput_antinodes(p1,p2,part))
    return antinodes
        


def select_good_antinodes(antinodes):
    antinodes = antinodes[is_inside(antinodes, border)]
    # for frequency in frequencies:
    #     positions = antenna[frequency]['pos']
    #     conds = [np.any(antinodes!=pos, axis=1) for pos in positions]
    #     antinodes = antinodes[np.all(conds, axis=0)]
    return antinodes



# Part 1 & 2
part = 2
antinodes = []
for frequency in frequencies:
    positions = antenna[frequency]['pos']
    antinodes += find_antinodes(positions, part=part)
antinodes = np.unique(np.concatenate(antinodes), axis=0)
antinodes = select_good_antinodes(antinodes)
print(f'Part {part}:', len(antinodes))



