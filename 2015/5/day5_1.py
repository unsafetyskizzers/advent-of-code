file = open("input.txt", "r")
nice_strings = []
naughty_strings = []

for line in file:
    nice_checklist = [0, 0, 1] # three vowels, double letter, blacklist pass
    vowel_counter = 0
    for i in range(len(line)):
        if i != 0:
            if line[i] == line[i-1]:
                nice_checklist[1] = 1
        if line[i] in "aeiou":
            vowel_counter += 1
        if vowel_counter >= 3:
            nice_checklist[0] = 1
    for combo in ["ab", "cd", "pq", "xy"]:
        if combo in line:
            nice_checklist[2] = 0
    if nice_checklist == [1, 1, 1]:
        nice_strings.append(line)
    else:
        naughty_strings.append(line)

print("Nice strings:", len(nice_strings))
print("Naughty strings:", len(naughty_strings))
