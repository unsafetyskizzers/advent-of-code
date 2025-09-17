file = open("input.txt", "r")
nice_strings = []
naughty_strings = []

for line in file:
    combo_dict = {}
    nice_checklist = [0, 0] # repeat pairs, valid triplets
    for i in range(len(line)):
        if i > 0:
            if (line[i-1] + line[i]) in combo_dict:
                    if combo_dict[line[i-1] + line[i]] != i-1:
                        nice_checklist[0] = 1
            else:
                combo_dict[line[i-1] + line[i]] = i
        if i > 1:
            if line[i-2] == line[i]:
                nice_checklist[1] = 1
    if nice_checklist == [1, 1]:
        nice_strings.append(line)
    else:
        naughty_strings.append(line)

print("Nice strings:", len(nice_strings))
print("Naughty strings:", len(naughty_strings))