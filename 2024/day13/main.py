import numpy as np
import re

arcades = []
with open('input.txt', 'r') as file:
    arcades = file.read().split('\n\n')
    arcades = [arc.split('\n') for arc in arcades]
button_token = np.array((3,1))

def get_token(buttons, price):
    if np.any(price<0): return -10000000
    division0 = np.divide(price,buttons[0])
    print(division0)
    division1 = np.divide(price,buttons[1])
    if division0[0]==division0[1]: 
        return division0[0]*button_token[0]
    else:
        return button_token[1] + get_token(buttons, price-buttons[1])



def mathematic_method(buttons, price):
    ''' buttons * solution = price '''
    buttons = np.matrix(buttons)
    price = np.matrix(price)
    solution = np.matmul(buttons.T.getI(),price.T)
    print(buttons, price, solution, sep=' - ')
    print()
    solution = np.squeeze(np.asarray(np.rint(solution)))
    if not np.all(solution*buttons == price): 
        print(buttons, price, solution, sep=' - ')
        print(solution*buttons)
        return 0
    token = np.sum(solution*button_token)
    return int(token)




def do_part(part = 1):
    total_token = 0
    for arc in arcades:
        buttons, price = arc[:2], arc[2]
        buttons = np.array([re.findall('[0-9]+',b)
                    for b in buttons],dtype=int)
        price = np.array(re.findall('[0-9]+',price),dtype=int)
        if part==2: price += 10000000000000 
        print(price)
        token = mathematic_method(buttons, price)
        print(token)
        total_token += token

    return total_token


print('Part 1:', do_part(part=2))