import math

file = open("2015/17/input.txt", "r")
input = file.readlines()
file.close()

containers = [] # capacities identified by index as id
combo_list = []

for i in range(len(input)):
    containers.append(int(input[i].strip()))

print(containers)

for i in range(0, len(containers)):
    #print(list(range(len(containers) - i + 1, len(containers) + 1)))
    combo = []
    total_volume = []
    for ii in range(0, i+1):
        combo.append(ii)
    while combo != list(range(len(containers) - i - 1, len(containers))):
        #print(combo)
        total_volume = []
        for ii in combo:
            total_volume.append(containers[ii])
        if sum(total_volume) == 150:
            combo_list.append(combo.copy())
        if combo[-1] == len(containers) - 1:
            for ii in range(i, -1, -1):
                if combo[ii] != len(containers) - i + ii - 1:
                    combo[ii] += 1
                    for iii in range(ii+1, i+1):
                        combo[iii] = combo[iii-1] + 1
                    break
        else:
            combo[-1] += 1

combos = 0
min_number = 999
min_number_combos = 0

for i in combo_list:
    combos += 1
    if min_number >= len(i):
        min_number = len(i)
        min_number_combos += 1

print(combos, min_number_combos)