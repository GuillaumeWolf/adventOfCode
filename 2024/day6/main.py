import numpy as np

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
                print('\033[31m', box, '\033[0m')
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
    return map, not in_map_range(new_coordonnee, map)


show(map)

# Part 1: solve
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




