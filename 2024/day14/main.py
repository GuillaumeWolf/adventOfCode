import numpy as np
import re 
import time
from itertools import product


robots = []
# shap = np.array((11,7))
shap = np.array((101,103))
t = 100
with open('input.txt', 'r') as file:
    for line in file:
        pos, v = line.strip().split(' ')
        robots.append({
            'pos': np.array(tuple(map(int,re.findall('[0-9]+',pos)))), 
            'v': np.array(tuple(map(int,re.findall('[-]?[0-9]+',v)))), 
        })
# print(*robots,sep='\n')


def move_robot(robot, t=t):
    x,v = robot['pos'],robot['v']
    final_pos = (x + v*t)
    final_pos = final_pos%shap
    return final_pos

def get_quadrant(pos):
    quadrants = np.zeros((4))
    if np.any(pos==shap//2): return quadrants
    i = sum(np.multiply(pos<shap//2, np.array((1,2))))
    quadrants[i] = 1
    return quadrants

def affiche_step(robots, file=None, t=0):   
    room = np.zeros(shap)
    for r in robots:
        room[*r['pos']] += 1
    if not np.any(np.count_nonzero(room,axis=0)>=33): return
    
    for i in np.arange(shap[0]):
        for j in np.arange(shap[1]):
            if room[i,j]==1:
                if file==None:
                    print('\033[92mo', end='')
                else:
                    file.write('o')
            else:
                if file==None:
                    print('\033[31m ', end='')
                else:
                    file.write(' ')
        if file==None:
            print()
        else:
            file.write('\n')
    print('\033[0m\n')
    print('t =',t)


# Part 1
# quadrants = np.zeros((4))
# print(quadrants)
# for r in robots:
#     final_pos = move_robot(r)
#     quadrants += get_quadrant(final_pos)

# print(quadrants)
# print(np.prod(quadrants))





# Part 2

# f = open("tree.txt", "w")
# f.write(' ')
# f.close()

for t in range(1,5000):
    for k,r in enumerate(robots):
        robots[k]['pos'] = move_robot(r)

    affiche_step(robots, t=t)

    # if t%103==18:
    #     f = open("tree.txt", "a")
    #     f.write(f'{t}\n')
    #     affiche_step(robots, file=f)
    #     f.write('\n\n\n')
    #     f.close()



