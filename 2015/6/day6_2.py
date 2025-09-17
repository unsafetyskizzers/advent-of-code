file = open("input.txt", "r")

lights = []

for x in range(1000):
    lights.append([])
    for y in range(1000):
        lights[x].append(0)

for line in file:
    command = line.strip().split(" ")
    if command[0] == "turn":
        start_coords = command[2].split(",")
        end_coords = command[4].split(",") # index 3 is "through"
        for x in range(int(start_coords[0]), int(end_coords[0])+1):
            for y in range(int(start_coords[1]), int(end_coords[1])+1):
                if command[1] == "off" and lights[x][y] > 0:
                    lights[x][y] -= 1
                elif command[1] == "on":
                    lights[x][y] += 1
    elif command[0] == "toggle":
        start_coords = command[1].split(",")
        end_coords = command[3].split(",") # index 2 is "through"
        for x in range(int(start_coords[0]), int(end_coords[0])+1):
            for y in range(int(start_coords[1]), int(end_coords[1])+1):
                lights[x][y] += 2

brightness = 0
for x in range(1000):
    for y in range(1000):
        brightness += lights[x][y]

print("Total brightness:", brightness)

