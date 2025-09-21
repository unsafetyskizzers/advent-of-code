file = open("2015/13/input.txt", "r")
input = file.readlines()
file.close()

net_happiness_map = {}

for line in input:
    command = line.split()
    command[10] = command[10].strip(".")
    happy_delta = int(command[3])
    if command[2] == "lose":
        happy_delta *= -1
    if command[0] in net_happiness_map:
        if command[10] in net_happiness_map[command[0]]:
            net_happiness_map[command[0]][command[10]] += happy_delta
        else:
            net_happiness_map[command[0]][command[10]] = happy_delta
    else:
        net_happiness_map[command[0]] = { command[10]: happy_delta }
    if command[10] in net_happiness_map:
        if command[0] in net_happiness_map[command[10]]:
            net_happiness_map[command[10]][command[0]] += happy_delta
        else:
            net_happiness_map[command[10]][command[0]] = happy_delta
    else:
        net_happiness_map[command[10]] = { command[0]: happy_delta }

print(net_happiness_map)

def greedy_arrangement(curr_arr, all_guests):
    if len(curr_arr) == len(all_guests):
        return curr_arr
    else:
        new_arr = curr_arr.copy()
        curr_guest = curr_arr[-1]
        best_happy_delta = -999999
        best_happy_delta_guest = ""
        for guest in all_guests:
            if guest != curr_guest and guest not in curr_arr:
                if net_happiness_map[curr_guest][guest] > best_happy_delta:
                    best_happy_delta = net_happiness_map[curr_guest][guest]
                    best_happy_delta_guest = guest
        new_arr.append(best_happy_delta_guest)
        return greedy_arrangement(new_arr, all_guests)

seating_arrangements = []
for guest in net_happiness_map.keys():
    seating_arrangements.append(greedy_arrangement([guest], net_happiness_map.keys()))

best_arrangement = []
best_arrangement_happiness = 0
for arr in seating_arrangements:
    arrangement_happiness = 0
    for i in range(len(arr)):
        arrangement_happiness += net_happiness_map[arr[i]][arr[i-1]]
    if arrangement_happiness > best_arrangement_happiness:
        best_arrangement_happiness = arrangement_happiness
        best_arrangement = arr

print("Best arrangement:", best_arrangement, "with score", best_arrangement_happiness)