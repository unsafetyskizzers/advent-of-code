import copy

file = open("2015/18/input.txt", "r")
input = file.readlines()
file.close()

lights = []

#set up light grid
for i in range(len(input)):
    lights.append([])
    for ii in range(len(input[i].strip())):
        if input[i][ii] == "#":
            lights[i].append(True)
        elif input[i][ii] == ".":
            lights[i].append(False)

new_lights = copy.deepcopy(lights)

for i in range(100):
    for x in range(len(lights)):
        for y in range(len(lights[x])):
            lit_neighbors = 0
            x_indices = []
            y_indices = []
            if x == 0:
                x_indices = [0, 1]
            elif x == 99:
                x_indices = [98, 99]
            else:
                x_indices = [x-1, x, x+1]
            
            if y == 0:
                y_indices = [0, 1]
            elif y == 99:
                y_indices = [98, 99]
            else:
                y_indices = [y-1, y, y+1]

            for ix in x_indices:
                for iy in y_indices:
                    if not (ix == x and iy == y):
                        if lights[ix][iy] == True: lit_neighbors += 1
            if x in [0, 99] and y in [0, 99]:
                new_lights[x][y] = True
            elif lights[x][y] == True:
                if lit_neighbors in [2, 3]:
                    new_lights[x][y] = True
                else:
                    new_lights[x][y] = False
            else:
                if lit_neighbors == 3:
                    new_lights[x][y] = True
                else:
                    new_lights[x][y] = False
            
    lights = copy.deepcopy(new_lights)

final_light_count = 0
for x in lights:
    for y in x:
        if y == True:
            final_light_count += 1
print(final_light_count)