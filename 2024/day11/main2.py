import numpy as np
import sys, os

def disablePrint():
    sys.stdout = open(os.devnull, 'w')
def enablePrint():
    sys.stdout = sys.__stdout__



initial_stones = []
with open('input.txt', 'r') as file:
    initial_stones.append(file.read().strip().split())
initial_stones = initial_stones[0]


def split_stone(stone):
    l = len(stone)
    first, second = stone[:l//2], stone[l//2:]
    while second!='0' and second[0]=='0': 
        second = second[1:]
    return first, second

def change_stone(stone):
    new_stones = tuple()
    if stone=='0': new_stones = ('1', )
    elif len(stone)%2==0: 
        new_stones = split_stone(stone)
    else: new_stones = (str(int(stone)*2024), )
    return new_stones

def blink(stones, next_stone_dic, show=False):
    if not show: disablePrint()
    new_stones = []
    for s in stones:
        print(f'{s = }')
        changed_stone = change_stone(s)
        next_stone_dic[s] = changed_stone
        for cs in changed_stone:
            if (cs not in next_stone_dic.keys() 
                and cs not in new_stones):
                new_stones.append(cs)
    if not show: enablePrint()
    return new_stones, next_stone_dic



def recursive_path(stone, next_stone_dic, depth, n_blink):
    if depth==n_blink: return 1
    sum_stone = 0
    for next_stone in next_stone_dic[stone]:
        # print(f'({depth})', stone, ':', next_stone)
        sum_stone += recursive_path(next_stone, 
                                    next_stone_dic, 
                                    depth+1, 
                                    n_blink)
    # print(f'({depth})',sum_stone)
    return sum_stone



stones = initial_stones
next_stone_dic = {}
n_blink = 75
for i in range(n_blink):
    # print(stones)
    # print(next_stone_dic)  
    stones, next_stone_dic = blink(stones, 
                                    next_stone_dic, 
                                    show=False)
print(*next_stone_dic.items(), sep='\n')  
    
sum_stone = 0
for stone in initial_stones:
    sum_stone += recursive_path(stone, 
                                next_stone_dic, 
                                0, 
                                n_blink)
print(f'{sum_stone = }')
 

