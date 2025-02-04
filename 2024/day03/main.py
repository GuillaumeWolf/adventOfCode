import re 


text = ''

with open('input.txt','r') as file:
    text = file.read()


# Part 1: solve
muls = re.findall('mul\([0-9]+,[0-9]+\)', text)
nums = [re.findall('[0-9]+', x) for x in muls]
multiplied = [int(n[0])*int(n[1]) for n in nums]
print('Part 1:', sum(multiplied))



#Part 2: solve
tot = 0
muls = re.findall("mul\([0-9]+,[0-9]+\)|do(?:n't)?\(\)", text)
do = True
for word in muls:
    if do and re.search("[0-9]+", word):
        nums = re.findall("[0-9]+", word)
        tot += int(nums[0])*int(nums[1])
    if re.search("do(?:n't)?\(\)", word): 
        do = re.search("do\(\)", word)
print('Part2:', tot)