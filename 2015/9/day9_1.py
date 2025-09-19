file = open("2015/9/input.txt", "r")
input = file.readlines()
file.close()

edges = {}

for line in input:
    command = line.split(" ")
    if command[0] not in edges:
        edges[command[0]] = {}
    if command[2] not in edges:
        edges[command[2]] = {}
    if command[2] not in edges[command[0]]:
        edges[command[0]][command[2]] = int(command[4])
    if command[0] not in edges[command[2]]:
        edges[command[2]][command[0]] = int(command[4])

locations = edges.keys()
possible_routes = []
shortest_route = []
shortest_route_length = 999999
longest_route = []
longest_route_length = 0

def all_subroutes(curr_route, full_route):
    if len(curr_route) != len(full_route):
        for dest in full_route:
            if dest not in curr_route:
                new_curr_route = curr_route.copy()
                new_curr_route.append(dest)
                all_subroutes(new_curr_route, full_route)
    else:
        possible_routes.append(curr_route)

for loc in locations:
    all_subroutes([loc], locations)

for route in possible_routes:
    route_length = 0
    for i in range(len(route)-1): 
        route_length += edges[route[i]][route[i+1]]
    if route_length < shortest_route_length:
        shortest_route_length = route_length
        shortest_route = route

print("Shortest route:", shortest_route, "of length", shortest_route_length)

for route in possible_routes:
    route_length = 0
    for i in range(len(route)-1): 
        route_length += edges[route[i]][route[i+1]]
    if route_length > longest_route_length:
        longest_route_length = route_length
        longest_route = route

print("Longest route:", longest_route, "of length", longest_route_length)