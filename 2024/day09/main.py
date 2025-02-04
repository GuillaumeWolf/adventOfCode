import numpy as np 
import awkward as ak


disk = []
with open('input.txt', 'r') as file:
    disk = [int(char) for char in file.read()]
disk = np.array(disk)






def find_first_free_space(disk, i=0, k=1000):
    js = np.where((disk!=0) & (disk>=k))[0]
    js = js[(js>=i) & (js%2==1)]
    if not np.any(js): 
        return None
    return js[0]

def find_first_free_space2(disk, k=1000):
    js = np.where((disk[:,0]>=k) & (disk[:,1]==False))[0]
    if not np.any(js): 
        return None
    return js[0]


def is_there_small_file_after_i(disk, space=10, i=0):
    i = i+i%2
    return any((disk[i::2]<=space) & (disk[i::2]!=0))


def add_to_checksum(x, checksum, count):
    checksum += x*count
    count += 1
    return checksum, count



def concatenate_free_space(disk, coeffs):
    i=0
    while i<disk.shape[0]:
        if i%2!=0 and i+2<disk.shape[0] and disk[i+1]==0: 
            disk[i] += disk[i+2]
            disk[i+2] = 0
            disk = np.concatenate([disk[:i+1],disk[i+3:]])
            coeffs = np.concatenate([coeffs[:i+1],coeffs[i+3:]])
        else: i += 1
    return disk, coeffs


# correct
def affiche(arr, name=None, colorless=False):
    if not name is None:
        print(name,': ', sep='', end='')
    else: name = ''
    for i in range(arr.shape[0]):
        if i%2==0:
            print('\033[31m', end='')
        elif not colorless:
            print('\033[92m', end='')
        if name.strip()=='coeff' and i%2==1:
            print(' ', end=' ')
        else:
            print(arr[i], end=' ')
    print('\033[0m')

def affiche2(disk):
    for k in (0,2):
        for i in range(disk.shape[0]):
            if disk[i,1]:
                print('\033[31m', end='')
                print(disk[i,k], end= ' ')
            elif k==0:
                print('\033[92m', end='')
                print(disk[i,k], end= ' ')
            else:
                print(' ', end= ' ')
        print()
    print('\033[0m')

def compute_checksum(files, values):
    print(f'{files = }')
    print(f'{values = }')
    cumulate = np.cumsum(files)
    count = np.concatenate([[0], cumulate[:-1]])
    print(f'{count = }')
    print(values, '(', count*files, (files-1)*files//2, ')')
    checksum = np.sum(values*(count*files + (files-1)*files//2))
    return checksum

def find_last_file(disk):
    js = np.where(disk!=0)[0]
    js = js[js%2==0]
    if not np.any(js): 
        return None
    return js[-1]

def find_first_freespace(disk):
    js = np.where(disk!=0)[0]
    js = js[js%2==1]
    if not np.any(js): 
        return None
    return js[0]

def change_memory(disk, file_i, free_i, to_move):
    disk[file_i] -= to_move
    disk[free_i] -= to_move
    disk = np.insert(disk, free_i, to_move)
    disk = np.insert(disk, free_i, 0)
    return disk

def change_coeff(disk, free_i, coeff):
    disk = np.insert(disk, free_i, coeff)
    disk = np.insert(disk, free_i, 0)
    return disk



# Part 1
def part1(disk):
    coeffs = np.array([i//2 for i in range(disk.shape[0])])
    # affiche(disk, 'disk  ')
    # affiche(coeffs, 'coeff ')
    while find_last_file(disk)>find_first_freespace(disk):
        file_i, free_i = find_last_file(disk),find_first_freespace(disk)
        file_space, free_space = disk[file_i], disk[free_i]
        to_move = min(file_space, free_space)
        coeff = coeffs[file_i]
        # Change the disk memory
        disk = change_memory(disk, file_i, free_i, to_move)
        coeffs = change_coeff(coeffs, free_i, coeff)
        if find_last_file(disk) is None or find_first_freespace(disk) is None:
            break
            
    affiche(disk[::2], 'sub-disk  ', colorless=True)
    affiche(coeffs[::2], 'sub-coeff ', colorless=True)
    print(compute_checksum(disk[::2], coeffs[::2]))
 
 
# part1(disk=disk)




# Part 2
def part2(disk):
    coeffs = np.array([i//2 for i in range(disk.shape[0])])
    disk = np.array([[disk[i], i%2==0, coeffs[i]] 
            for i in range(disk.shape[0])])
    file_space_index = np.where(disk[:,1])[0]
    for j in range(file_space_index.shape[0]-1,-1,-1):
        # affiche2(disk)
        file_i = file_space_index[j]
        free_i = find_first_free_space2(disk, k=disk[file_i,0])
        if free_i is None: continue
        if free_i<file_i:
            if disk[free_i,0] > disk[file_i,0]:
                to_insert = np.array([disk[free_i,0] - disk[file_i,0], False, 0])
                disk = np.insert(disk, free_i+1, to_insert, axis=0)
                file_i += 1
                file_space_index[file_space_index>free_i] += 1
            disk[free_i] = disk[file_i]
            disk[file_i,1] = False
    
    disk[np.where(disk[:,1]==False),2] *= 0
    disk[np.where(disk[:,1]==False),1] = True
    disk[disk[:,1]==False][:,1] = True
    affiche2(disk)
    disk = disk[disk[:,1]==True]
    affiche2(disk)
    print(compute_checksum(disk[:,0], disk[:,2]))





part2(disk=disk)







