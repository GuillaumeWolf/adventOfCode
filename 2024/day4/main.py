import numpy as np
import re

def check(i,j,data):
    tot = 0
    words = []
    if i+4<=data.shape[0]:
        words.append(''.join(data[i:i+4,j]))
        if j+4<=data.shape[1]:
            words.append(''.join(data[i:i+4,j:j+4]
                                 [np.eye(4, dtype=bool)]))
        if j-3>=0:
            words.append(''.join(data[i:i+4,j-3:j+1]
                                 [np.flip(np.eye(4, dtype=bool),0)]))
    if j+4<=data.shape[1]:
        words.append(''.join(data[i,j:j+4]))
        
    # print(words)
    for w in words:
        if w=='XMAS' or w=='SAMX':
            tot += 1
    return tot


def show_X_mas(data, i=0, j=0, color='\033[92m'):
    for a in range(data.shape[0]):
        print()
        for b in range(data.shape[1]):
            if ((a==i or a==i+2) and (b==j or b==j+2)) or (a==i+1 and b==j+1):
                print(color, end='')
                print(data[a,b], end=' ')
            else: print(' ', end=' ')
            if a>=i and a<i+3 and b>=j and b<j+3:
                print('\033[0m', end='')
    print()


def check2(i,j,data):
    chars = data[i-1:i+2,j-1:j+2]
    if (   i==0 
        or j==0 
        or i==data.shape[0]-1
        or j==data.shape[1]-1):
        return 0
    if not data[i,j]=='A': return 0
    diags = ((i-1,j-1), (i-1,j+1), (i+1,j-1), (i+1,j+1))
    for d in diags:
        if not data[d] in ('M', 'S'): 
            show_X_mas(chars,color='\033[31m') # display
            return 0
    x = [data[d] for d in diags]
    if not (x==['M','S','M','S'] 
            or x==['S','M','S','M']
            or x==['S','S','M','M']
            or x==['M','M','S','S']):
        show_X_mas(chars,color='\033[33m') # display
        return 0
    show_X_mas(chars) # display
    return 1



# Input
data = []
with open('input.txt', 'r') as file:
    for line in file:
        data.append([char for char in line if not char=='\n'])
data = np.array(data)



# Part1: solve
n_XMAS = 0
for i,line in enumerate(data):
    for j,char in enumerate(line):
        n_XMAS += check (i,j,data)

print('Part 1:', n_XMAS)




# Part2: solve
n_XMAS = 0
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        x = check2(i,j,data)
        n_XMAS += x

print('Part 2:', n_XMAS)


