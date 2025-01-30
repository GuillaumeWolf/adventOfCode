import numpy as np
import awkward as ak

rules = []
updates = []

# Get inputs
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



# Part 1
def correctly_ordered(update, rules):
    valide_rule = np.ones(np.shape(rules)[0], dtype=bool)
    for i, rule in enumerate(rules):
        if not np.all([n in update for n in rule]):
            continue 
        ind = [np.where(update==n)[0][0] for n in rule]
        if ind[1]<ind[0]:
            valide_rule[i] = False
    return valide_rule


def get_error(valide_rule):
    if np.all(valide_rule):
        return 0
    count = 0
    for vr in valide_rule:
        count += 0 if vr else 1
    return count



def correct(update, rules, valide_rule):
    unvalide_rules = rules[valide_rule==False]
    n_errors = get_error(valide_rule)
    n_errors_new = n_errors
    print(f'Unvalide rules: {unvalide_rules}')
    for ur in unvalide_rules:
        while n_errors<=n_errors_new:
            m=0


sum = 0
print(*rules, sep='\n')
for update in updates:
    print('update = ', update)
    valide_rule = correctly_ordered(update, rules)
    n_errors = get_error(valide_rule)
    print(f'{n_errors} updates are not valide !')
    # if not n_errors==0: 
    #     correct(update, rules, valide_rule)

    sum += update[int((len(update)-1)/2)]
    print()
    print()
    print()


print(sum)

