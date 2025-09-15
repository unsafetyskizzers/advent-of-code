file = open("route.txt", "r")
route = file.read()
file.close()

santa_pos = [0, 0]
robo_pos = [0, 0]
houses_visited = [[0, 0]]
turn = 0

for direc in route:
    move = [0, 0]
    match direc:
        case "^":
            move[1] += 1
        case "v":
            move[1] -= 1
        case "<":
            move[0] -= 1
        case ">":
            move[0] += 1
    if turn % 2 == 0:
        santa_pos = [santa_pos[0] + move[0], santa_pos[1] + move[1]]
    else:
        robo_pos = [robo_pos[0] + move[0], robo_pos[1] + move[1]]
    if santa_pos not in houses_visited:
        houses_visited.append(santa_pos.copy())
    if robo_pos not in houses_visited:
        houses_visited.append(robo_pos.copy())
    turn += 1

print(len(houses_visited))
input()