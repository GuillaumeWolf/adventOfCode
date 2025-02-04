import numpy as np
import time 


data = open('input.txt', 'r').read().split('\n')
# print(f'{data = }')

n_equ = len(data)
print(f'{n_equ = }')
equations = {}
equations['goal'] = [int(line.split(':')[0]) for line in data] 
equations['nums'] = [list(map(int, line.split(':')[1].split())) for line in data]
# print(f'{equations = }')


def multipla(a,b):
    return a*b

def sumpla(a,b):
    return a + b

def concapla(a,b):
    p10 = np.floor(np.log10(b)) + 1
    return int(a*10**p10 + b)


funcs = (multipla, sumpla)
def check(goal, inter_prod, nums, funcs=funcs):
    # print(goal, inter_prod, nums)
    if len(nums)==0: return goal==inter_prod
    goal_reached = []
    for func in funcs:
        # print(func.__name__)
        new_inter_prod = func(inter_prod, nums[0])
        if new_inter_prod>goal: continue
        goal_reached.append(check(goal, new_inter_prod, nums[1:], funcs=funcs))
    # print() 
    return any(goal_reached)


tot = 0
t0 = time.time()
for i in range(n_equ):
    # print('\033[1m', end='')
    # print(equations['goal'][i], equations['nums'][i])
    # print('\033[0m', end='')
    if check(equations['goal'][i], equations['nums'][i][0], equations['nums'][i][1:]):
        tot += equations['goal'][i]
    # print()
print(tot)
t1 = time.time()
print(f'Part 1 took {t1-t0:.4f} s')



funcs2 = (multipla, sumpla, concapla)
tot = 0
t0 = time.time()
for i in range(n_equ):
    # print('\033[1m', end='')
    # print(equations['goal'][i], equations['nums'][i])
    # print('\033[0m', end='')
    if check(equations['goal'][i], 
             equations['nums'][i][0], 
             equations['nums'][i][1:], 
             funcs=funcs2):
        tot += equations['goal'][i]
    # print()
print(tot)
t1 = time.time()
print(f'Part 2 took {t1-t0:.4f} s')
