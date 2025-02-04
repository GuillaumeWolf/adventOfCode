import numpy as np
import awkward as ak

rules = []
updates = []

# Get inputs
with open('input.txt', 'r') as file:
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


def get_unvalide_rules(update, rules):
    valide_rule = correctly_ordered(update, rules)
    return rules[valide_rule==False]
    

def correct(update, rules):
    initial_update = update.copy()
    valide_rule = correctly_ordered(update, rules)
    unvalide_rules = rules[valide_rule==False]
    # print(unvalide_rules)
    n_errors = get_error(valide_rule)
    # print(f'Unvalide rules: {unvalide_rules}')
    k = 0
    while get_error(correctly_ordered(update, rules))>0:
        # print(f'{n_errors} rule{('s, are' if n_errors>1 else ' is')} not valide !', unvalide_rules)
        ind = [np.where(update==n)[0][0] 
               for n in unvalide_rules[k]]
        # print(ind, unvalide_rules[k])
        # Lowering
        if not ind[0]==0:
            # print('(Lowering)')
            new_update = update.copy()
            n_minus1 = new_update[ind[0]-1]
            n = new_update[ind[0]]
            new_update[ind[0]] = n_minus1
            new_update[ind[0]-1] = n
            new_n_error = get_error(correctly_ordered(new_update, rules)) 
            if new_n_error<=n_errors:
                # print('Previous update: ', update)
                # print('New update: ', new_update)
                update = new_update.copy()
                n_errors = new_n_error
        # Raising
        if not ind[1]+1==len(update):
            # print('(Raising)')
            new_update = update.copy()
            n_plus1 = new_update[ind[1]+1]
            n = new_update[ind[1]]
            new_update[ind[1]] = n_plus1
            new_update[ind[1]+1] = n
            new_n_error = get_error(correctly_ordered(new_update, rules)) 
            if new_n_error<=n_errors:
                # print('Previous update: ', update)
                # print('New update: ', new_update)
                update = new_update.copy()
                n_errors = new_n_error
        
        # check for any changes
        # print(f'{initial_update = } at the begening of the loop. ')
        # print(f'{update = } at the end of the loop. ')
        if update==initial_update:
            # print('No change happened, changing rule')
            k+=1
        else: 
            unvalide_rules = get_unvalide_rules(update, rules)
            initial_update = update.copy()
            k=0
        # print('end of one loop')

    print('Final update:', update, f',  {n_errors = }')
    return update




sum = [0,0]
print(*rules, sep='\n')
for update in updates:
    print('update = ', update)
    n_errors = get_error(correctly_ordered(update, rules))
    if n_errors>0: 
        print(f'{n_errors} rule{('s are' if n_errors>1 else ' is')} not satisfied !')
        update = correct(update, rules)
        sum[1] += update[int((len(update)-1)/2)]
    else: 
        print('The update is valide !')
        sum[0] += update[int((len(update)-1)/2)]
    print()
    print()
    print()


print(sum)








