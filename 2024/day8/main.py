import numpy as np
import awkward as ak
from itertools import product as it_prod

def is_inside(pos, border):
    cond1 = np.all(pos>=0, axis=1)
    cond2 = np.all(pos<border, axis=1)
    result = np.all((cond1, cond2), axis=0)
    return result




data = []
with open('input.txt', 'r') as file:
    for line in file:
        data.append([char for char in line.strip()])
data = np.array(data)

city = []
frequencies = []
border = data.shape
for i in range(border[0]):
    for j in range(border[0]):
        city.append({'i': i, 'j': j, 'f': data[i][j]})
        if not data[i][j]=='.': frequencies.append(data[i][j])


city = ak.Array(city)
frequencies = set(frequencies)

print(f'{border = }')
print(f'{city = }')
print(f'{frequencies = }')


def comput_antinodes(p1,p2):
    dp = p2-p1
    return (p1-dp, p2+dp) 



def find_antinodes(frequency, positions):
    antinodes = []
    for p1,p2 in it_prod(positions,positions):
        antinodes.append(comput_antinodes(p1,p2))
    return antinodes



antinodes = []
for frequency in frequencies:
    positions = np.transpose([city[city['f']==frequency][ind] 
                 for ind in ('i', 'j')])
    antinodes += find_antinodes(frequency, positions)

antinodes = np.unique(np.concatenate(antinodes), axis=0)
print(antinodes[is_inside(antinodes, border)])
print(len(antinodes[is_inside(antinodes, border)]))





