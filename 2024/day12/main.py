import numpy as np
from itertools import product, combinations
import sys, os

def disablePrint():
    sys.stdout = open(os.devnull, 'w')
def enablePrint():
    sys.stdout = sys.__stdout__


garden = []
with open('input.txt', 'r') as file:
    for line in file:
        garden.append([*line.strip()])
garden = np.array(garden)
# print(garden)
if garden.shape[0]>15: disablePrint()



def affiche_region(r):
    for i in range(r.shape[0]):
        for j in range(r.shape[1]):
            if r[i,j]==True:
                print('\033[92m[]', end='')
            else:
                print('\033[31m[]', end='')
        print()
    print()
    print('\033[0m')

sides = np.array(
    ((0,1), (0,-1), (1,0), (-1,0))
)

def inside_garden(pos, shap, axis=0):
    return np.all((pos>=0) & (pos<shap), axis=axis)

def find_regions(pos, garden, region=None):
    # print(pos, region)
    shap = garden.shape
    if region is None: region = np.zeros(shap, dtype=bool)
    region[*pos] = True
    for s in sides:
        new_pos = pos + s
        if (inside_garden(new_pos, shap)
            and garden[*pos]==garden[*new_pos]
            and region[*new_pos]==False):
            region = find_regions(new_pos, garden, region=region)
    return region



# separate the regions
inds = tuple(np.arange(garden.shape[k]) for k in (0,1)) 
indy = np.arange(garden.shape[1])
n_region = 0
regions = np.array([])
for i,j in product(*inds):
    if (i,j)!=(0,0) and np.any(regions==True,axis=0)[i,j]: 
        continue
    r = find_regions((i,j), garden)
    if len(regions)==0: regions = np.array([r])
    else:
        regions = np.insert(regions, -1, r, axis=0)


#Perimeter func
def get_per(pos, r):
    new_pos = pos+sides
    new_pos = new_pos[inside_garden(new_pos,r.shape, axis=1)]
    new_pos = np.column_stack(new_pos)
    return 4 - np.count_nonzero(r[*new_pos]==True)


def get_corner(pos, r):
    print(f'{pos = }')
    corner_val = 0
    for s1,s2 in combinations(sides,2):
        if np.any(s1==s2): continue
        diag = pos+s1+s2
        if inside_garden(diag,r.shape) or r[*diag]==True: 
            print('diag True', diag)
            continue
        else: print('diag False', diag)
        sid = np.column_stack([pos+s1, pos+s2])
        print(sid)
        if np.all(r[*sid]==True):
            print('sid True', pos,s1,s2)
        if np.all(r[*sid]==False):
            print('sid False', pos,s1,s2)
    print()
    print()
    print()
    return 0


# measure the area, perimeter and length of each regions
areas = [np.count_nonzero(r) for r in regions]
perimeters = []
n_sides = []
for k,r in enumerate(regions):
    print(k,':')
    affiche_region(r)
    perimeters.append(0)
    for i,j in zip(*np.where(r==True)):
        perimeters[-1] += get_per((i,j), r)
        get_corner((i,j), r)
        




# final prints
areas = np.array(areas)
perimeters = np.array(perimeters)

print(areas)
print(perimeters)



enablePrint()
print('Part 1:', sum(areas*perimeters))









