import numpy as np

# Get input 
reports = []
with open('input.txt','r') as file:
    for line in file:
        reports.append([int(x) for x in line.split()])




def safe_report(r):
    if len(r)==1: return True
    increasing = r[1]>r[0]
    for i in range(len(r)-1):
        if not(r[i+1]>r[i])==increasing: 
            return False
        if abs(r[i+1]-r[i])<1 or abs(r[i+1]-r[i])>3: 
            return False
    return True


# Part 1: solve
def part1(reports):  
    count = 0
    for r in reports:
        if safe_report(r): count += 1
    print(count)

# Part 2: solve
def part2(reports   ):
    count = 0
    for r in reports:
        safe = safe_report(r)
        if not safe_report(r): 
            for i in range(len(r)):
                safe = safe or safe_report(r[:i]+r[i+1:]) 
        if safe: count += 1
    print(count)



part1(reports)
part2(reports)