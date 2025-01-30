import numpy as np
import awkward as ak

rules = []
updates = []

with open('input2.txt', 'r') as file:
    for line in file:
        split = line.strip().split('|')
        if len(split)==2:
            rules.append([int(split[0]), int(split[1])])
        if len(split)==1 and not split==['']:
            updates.append([int(n) for n in split[0].split(',')])

rules = ak.Array(rules)

# print(rules[:5])
# print()
# print(*updates[:5], sep='\n')
# print()

def correctly_ordered(update, rules):
    validity = [True for _ in update]
    for n in update:
        for rule in rules[[n in r for r in rules]]:
            nfirst = rule[0]==n
            m = rule[1] if nfirst else rule[0]
            if not m in update: continue
            if not (update.index(n)<update.index(m))==nfirst:
                validity[update.index(n)] = False
                validity[update.index(m)] = False
            # print(n, m, update.index(n), update.index(m), update.index(n)<update.index(m), nfirst)
    # print(update)
    # print(validity)
    # print()
    return ak.Array(validity)


def correct(update, rules, validity):
    error = len(validity[validity==False])
    new_update = update.copy()
    for n in update:
        if validity[update.index(n)]: continue
        new_update.remove(n)
        new_update.insert(update.index(n)+1, n)
        new_validity = correctly_ordered(new_update, rules)
        new_error = len(new_validity[new_validity==False])
        print(validity, new_validity)
        print(error, new_error)

    return new_update    




sum = 0
print(*rules, sep='\n')
for update in updates:
    print('update = ', update)
    validity = correctly_ordered(update, rules)
    if not len(validity[validity==False])==0:
        correct(update, rules, validity)
    sum += update[int((len(update)-1)/2)]
    print()
    print()
    print()


