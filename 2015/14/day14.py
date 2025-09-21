file = open("2015/14/input.txt", "r")
input = file.readlines()
file.close()

reindeer_stats = {}

for line in input:
    command = line.split()
    reindeer_stats[command[0]] = { "speed": int(command[3]), "stamina": int(command[6]), "rest": int(command[13]) }

reindeer_position = {}
reindeer_score = {}

for deer in reindeer_stats.keys():
    reindeer_position[deer] = 0
    reindeer_score[deer] = 0

time = 0
while time < 2503:
    for deer in reindeer_position.keys():
        if time % (reindeer_stats[deer]["stamina"] + reindeer_stats[deer]["rest"]) < reindeer_stats[deer]["stamina"]:
            reindeer_position[deer] += reindeer_stats[deer]["speed"]
    high_dist = max(reindeer_position.values())
    for deer in reindeer_position.keys():
        if reindeer_position[deer] == high_dist:
            reindeer_score[deer] += 1
    time += 1

print(reindeer_position)
print(reindeer_score)
print("Fastest reindeer:", max(reindeer_position, key=reindeer_position.get), "at position", max(reindeer_position.values()))
print("Highest scoring reindeer:", max(reindeer_score, key=reindeer_score.get), "with score", max(reindeer_score.values()))