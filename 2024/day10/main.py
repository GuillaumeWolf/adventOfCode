import numpy as np

montains = []
with open('input.txt', 'r') as file:
    for line in file:
        montains.append(list(map(int,line.strip())))
montains = np.array(montains)



def is_inside(point, mapp):
    it_is = True
    if np.any(point<0): it_is = False
    if np.any(point>=mapp.shape): it_is = False
    return it_is


masks = (
    np.array((0,1)),
    np.array((0,-1)),
    np.array((1,0)),
    np.array((-1,0)),
)

def find_trails(starts, montains, k=0):
    ends = []
    for mask in masks:
        # print(starts, mask)
        # print(montains)
        isInside = is_inside(starts+mask, montains)

        if isInside and montains[*(starts+mask)]==k+1:
            if k+1==9: 
                # print('Find a point:', starts+mask)
                ends.append(starts+mask)
                # print(f'{ends = }')
            else:
                output = find_trails(starts+mask, montains, k+1)
                # print(f'{output = }')
                # print('before', ends)
                if np.any(output): 
                    # print('ends:', *ends)
                    # print('output:', output)
                    for op in output:
                        ends.append(op)
                # print('after', ends)
        # elif isInside:
        #     print(montains[*(starts+mask)], f'{k+1 = }')
    # print(f'{ends = }')
    return ends


part1_tot, part2_tot = 0, 0
for (i,j) in zip(*np.where(montains==0)):
    ends = find_trails((i,j), montains)
    # print('Output for ',i,j,':', ends)
    part1_tot += len(np.unique(ends, axis=0))
    part2_tot += len(ends)
print(f'{part1_tot = }')
print(f'{part2_tot = }')








