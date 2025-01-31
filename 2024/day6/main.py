import numpy as np
import time 


next_coor = {
    '^':np.array((-1,0)),
    'v':np.array((1,0)),
    '>':np.array((0,1)),
    '<':np.array((0,-1)),
}


# inputs
map = []
with open('input.txt') as file:
    for line in file:
        map.append([char for char in line.strip()])

map = np.array(map)


# Functions

def show(map):
    print(' ', end='')
    for _ in range(map.shape[1]):print('_', end='')
    print()
    for line in map:
        print('|', end='')
        for box in line:
            if box=='.': print(' ', end='')
            elif box in list(next_coor.keys()):
                print('\033[31m', box, '\033[0m', sep='', end='')
            else:print(box, end='')
        print('|')
    print(' ', end='')
    for _ in range(map.shape[1]):print('_', end='')
    print()


def path_length(map):
    return len(map[map=='X'])


def get_dir(map): 
    dir_poss = np.array(('^', '<', '>', 'v'))
    poss = list(dir in map for dir in dir_poss)
    dir = dir_poss[poss][0]
    return dir


def get_coordonnee(map):
    dir = get_dir(map)
    return np.array(np.concatenate(
        np.where(map==dir)))


def in_map_range(coor, map):
    if (not np.all(coor>=0)
        or not np.all(coor<map.shape)):
        return False
    return True


def make_a_step(map):
    coordonnee = get_coordonnee(map)
    dir = get_dir(map)
    next_dir = {
        '^':'>',
        'v':'<',
        '>':'v',
        '<':'^',
    }
    new_coordonnee = coordonnee + next_coor[dir]
    if in_map_range(new_coordonnee, map):
        # Change coordonne
        if map[*new_coordonnee]=='#':
            dir = next_dir[dir]
            new_coordonnee = coordonnee + next_coor[dir]
        map[*coordonnee] = 'X'
        map[*new_coordonnee] = dir
    return not in_map_range(new_coordonnee, map)


def mult(*input):
    a = 1
    for x in input:
        a *= x
    return a


def measure_time(func, funcname, *args, **kwargs):
    t0 = time.time()
    output = func(*args, **kwargs)
    t1 = time.time()
    print(f'func {funcname} took {(t1-t0)*1000:.1f} ms to run. ')
    return output


# Part 1: solve
if False:
    show(map)
    step = 0
    out = False
    while not out:
        # print(f'Step {step}')
        map, out = make_a_step(map)
        # show(map)
        # print('\n\n\n')
        step += 1 
    show(map)
    print(path_length(map)+1)




# Part 2: solve
box_that_loop = 0
print(map.shape)
start = {'coor': get_coordonnee(map), 'dir': get_dir(map)}
wall = [(i,j)
        for i in range(map.shape[0])
        for j in range(map.shape[1])
        if map[i,j]]
for i in range(map.shape[0]):
    for j in range(map.shape[1]):
        if (i,j) in wall: continue
        position = start.copy()
        print(i,j)
        looped = False
                
        
        t0 = time.time()
        map[i,j] = '#'
        out = False
        step = 0
        while not out and not looped:
            # print(step)
            out = make_a_step(map)
            step += 1 
            looped = step>(mult(*map.shape))
        if looped: 
            print('Loop found')
            show(map)
            box_that_loop += 1
        map[i,j] = '.'
        map[*get_coordonnee(map)] = '.'
        map[*start['coor']] = start['dir']
        t1 = time.time()
        print(f'Loop took {(t1-t0)*1000:.1f} ms to run. ')

print(box_that_loop)


