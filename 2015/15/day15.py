file = open("2015/15/input.txt", "r")
input = file.readlines()
file.close()

ingredients = {}
for line in input:
    command = line.split()
    ingredients[command[0].strip(":")] = {}
    for i in range(1, len(command), 2):
        ingredients[command[0].strip(":")][command[i]] = int(command[i+1].strip(","))

