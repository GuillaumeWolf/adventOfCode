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


def show_X_mas(data, i=-10, j=-10):
    for a in range(data.shape[0]):
        print()
        for b in range(data.shape[1]):
            if ((a==i or a==i+2) and (b==j or b==j+2)) or (a==i+1 and b==j+1):
                print('\033[92m', end='')
            print(data[a,b], end=' ')
            if a>=i and a<i+3 and b>=j and b<j+3:
                print('\033[0m', end='')
    print()


def check2(i,j,data):
    conds = ('i-1,j-1', 'i-1,j+1', 'i+1,j-1', 'i+1,j+1')
    for c in conds:
        if not data[eval(c)] in ('M', 'S'): 
            return 0
    x = [data[eval(c)] for c in conds]
    if x==['M','S','S','M'] or x==['S','M','M','S']:
        return 0
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
for i,line in enumerate(data):
    for j,char in enumerate(line):
        if (not i==0 and not j==0 
            and not i==data.shape[0]-1
            and not j==data.shape[1]-1
            and data[i,j]=='A'  ):
            n_XMAS += check2(i,j,data)

print('Part 2:', n_XMAS)


