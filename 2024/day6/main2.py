# import numpy as np


direction = ('^', 'v', '>', '<')

next_step = {}
next_step['position'] = {
    '^':(-1,0),
    'v':(1,0),
    '>':(0,1),
    '<':(0,-1),
}
next_step['direction'] = {
    '^':'>',
    'v':'<',
    '>':'v',
    '<':'^',
}


# inputs
map = []
with open('input.txt') as file:
    for line in file:
        map.append([char for char in line.strip()])

walls = []
starting = {}
border = (len(map), len(map[0]))
for i in range(border[0]):
    for j in range(border[1]):
        if map[i][j]=='#': walls.append((i,j))
        if map[i][j] in direction:
            starting['direction'] = map[i][j]
            starting['position'] = (i,j)

print(f'{border =}')
print(f'{walls =}')
print(f'{starting =}')


def is_inside(position, border):
    x = [position[i]>=0 and position[i]<border[i] for i in (0,1)]
    if x[0] and x[1]: return True
    return False


def add_positions(*positions):
    result = [0,0]
    for p in positions:
        for i in (0,1):
            result[i] += p[i]
    return tuple(result)


def make_path(starting, walls, border):
    visited_box = {'list': [starting['position']], 'times': [1]}
    # print(f'{visited_box = }')
    step = starting.copy()
    not_in_loop = True
    while is_inside(step['position'], border) and not_in_loop:
        new_position = add_positions(step['position'], 
                        next_step['position'][step['direction']])
        if new_position in walls:
            step['direction'] = next_step['direction'][step['direction']]
            new_position = add_positions(step['position'], 
                            next_step['position'][step['direction']])
        step['position'] = new_position
        if not new_position in visited_box['list']:
            visited_box['list'].append(new_position)
            visited_box['times'].append(1)
        else:
            idx = visited_box['list'].index(new_position)
            visited_box['times'][idx] += 1
        if 5 in visited_box['times']:
            not_in_loop = False


    return len(visited_box['list'])-1, not_in_loop, visited_box['list']




# Part 1
n_box_visited, not_in_loop, visited_box = make_path(starting, walls, border)
print(f'{n_box_visited = }')
print(f'{not_in_loop = }')


# Part 2
n_loop = 0
for i, box in enumerate(visited_box):
    if box in walls: continue
    print(f'{box} ({i}/{len(visited_box)})')
    walls.append(box)
    n_box_visited, not_in_loop, _ = make_path(starting, walls, border)
    in_loop = not not_in_loop
    if in_loop: 
        n_loop += 1
    walls.pop()
print(f'{n_loop = }')
