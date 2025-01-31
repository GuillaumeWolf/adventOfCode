import numpy as np
import time
from rich.progress import Progress, BarColumn, TextColumn
import awkward as ak


dirs = ('^', 'v', '>', '<')
dir_change = {
        '^':'>',
        'v':'<',
        '>':'v',
        '<':'^',
    }
step = {
    '^':np.array((-1,0)),
    'v':np.array((1,0)),
    '>':np.array((0,1)),
    '<':np.array((0,-1)),
}


def turn_right(dir):
    return dir_change[dir]

def move_forward(pos, dir):
    # pos = pos + step[dir]
    return pos + step[dir]

def move_backward(pos, dir):
    # pos = pos - step[dir]
    return pos - step[dir]


# inputs
map = []
with open('input.txt') as file:
    for line in file:
        map.append([char for char in line.strip()])

border = np.array((len(map), len(map[0])))
walls = np.array([[map[i][j]=='#' 
        for j in range(border[1])]
        for i in range(border[0])])
guard_start = {}
for i in range(border[0]):
    for j in range(border[1]):
        if map[i][j] in dirs:
            guard_start['pos'] = np.array((i,j))
            guard_start['dir'] = map[i][j]
visited_box = np.array([[0 
    for j in range(border[1])] 
    for i in range(border[0])
])

# print(f'{border =}')
# print(f'{walls =}')
# print(f'{guard_start =}')
# print(f'{visited_box =}')




def is_inside(pos, border=border):
    return np.all((pos>=0,pos<border))




def make_path(guard, walls=walls, border=border, return_path=False):
    visited_box = np.zeros(border)
    visited_box[*guard['pos']] += 1
    not_in_loop = True
    while (is_inside(move_forward(guard['pos'], guard['dir'])) 
           and not_in_loop):
        # print(f'{guard['pos'] = }')
        guard['pos'] = move_forward(guard['pos'], guard['dir']) 
        while walls[*guard['pos']]:
            guard['pos'] = move_backward(guard['pos'], guard['dir'])
            guard['dir'] = turn_right(guard['dir'])
            guard['pos'] = move_forward(guard['pos'], guard['dir']) 
        visited_box[*guard['pos']] += 1
        # print(f'{guard['pos'] = }')
        # print(f'{visited_box = }')
        if 5 in visited_box:
            not_in_loop = False
    # print(visited_box)
    if return_path:
        return np.count_nonzero(visited_box), visited_box
    return not_in_loop



# Part 1
t0 = time.time()
n_boxs, visited_box = make_path(guard_start.copy(), return_path=True)
print(f'{n_boxs = }')
print(f'{visited_box = }')
t1 = time.time()
print(f'Part 1 took {t1-t0:.4f} s')



# Part 2
t0 = time.time()
with Progress(
    TextColumn("[progress.description]{task.description}"),
    BarColumn(),
    TextColumn("{task.completed}/{task.total}"),
    transient=True 
    ) as progress:
    
    task = progress.add_task("[cyan]Processing...", total=n_boxs)
    n_loop = 0
    x,y = np.where(np.logical_not(visited_box==0))
    for i, j in zip(x,y):
        tloop0 = time.time()
        progress.update(task, advance=1)
        if np.array_equal(np.array([i, j]), guard_start['pos']): continue
        walls[i,j] = True
        not_in_loop = make_path(guard_start.copy(), walls=walls)
        if not not_in_loop:
            print('\033[1m', 'Was stucked in a loop. ', '\033[0m', sep='') 
            n_loop += 1
        walls[i,j] = False
        tloop1 = time.time()
        print(f'Loop ({i},{j}) took {tloop1-tloop0:.4f} s')

    print(f'{n_loop = }')
    with open('output2.txt', 'w') as output_file:
        output_file.write(str(n_loop))


t1 = time.time()
print(f'Part2 took {t1-t0:.4f} s')



