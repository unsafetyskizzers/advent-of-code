file = open("2015/16/aunts_sue.txt", "r")
aunts_list = file.readlines()
file.close()
file = open("2015/16/analysis.txt", "r")
analysis_list = file.readlines()
file.close()

aunts = {}
analysis = {}

for line in aunts_list:
    command = line.strip().split()
    for i in range(len(command)):
        command[i] = command[i].strip(":,")
    aunts[int(command[1])] = {}
    for i in range(2, len(command) - 1, 2):
        aunts[int(command[1])][command[i]] = int(command[i+1])

for line in analysis_list:
    command = line.strip().split()
    for i in range(len(command)):
        command[i] = command[i].strip(":,")
    for i in range(0, len(command), 2):
        analysis[command[i]] = int(command[i+1])

for aunt in aunts:
    aunt_matches = True
    for attr in aunts[aunt]:
        if attr == "cats" or attr == "trees":
            if aunts[aunt][attr] <= analysis[attr]:
                aunt_matches = False
        elif attr == "pomeranians" or attr == "goldfish":
            if aunts[aunt][attr] >= analysis[attr]:
                aunt_matches = False
        else:
            if aunts[aunt][attr] != analysis[attr]:
                aunt_matches = False
    if aunt_matches:
        print("Aunt match found:", aunt)
        break

    
        
    