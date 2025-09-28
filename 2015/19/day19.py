file = open("2015/19/input.txt", "r")
input = file.readlines()
file.close()

replacements = {}
medicine = ""
new_molecules = []

for line in input:
    line_str = line.strip()
    if line_str == "":
        break
    command = line_str.split()
    if command[0] in replacements:
        replacements[command[0]].append(command[2])
    else:
        replacements[command[0]] = [command[2]]

medicine = input[-1].strip()

print(replacements)
print(medicine)

for key in replacements.keys():
    new_molecule = ""
    if key in medicine:
        for i in range(len(medicine) - len(key) + 1):
            if medicine[i:i+len(key)] == key:
                for rep in replacements[key]:
                    new_molecule = medicine[0:i] + rep + medicine[i+len(key):]
                    if new_molecule not in new_molecules:
                        new_molecules.append(new_molecule)

print(len(new_molecules))

molecule_tree = ["e"]
new_molecule_tree = []
generation = 0

# NOTE: work BACKWARDS from finished molecule!!
while medicine not in molecule_tree:
    new_molecule_tree = []
    generation += 1
    for mol in molecule_tree:
        for key in replacements.keys():
            new_molecule = ""
            if key in mol:
                for i in range(len(medicine) - len(key) + 1):
                    if mol[i:i+len(key)] == key:
                        for rep in replacements[key]:
                            new_molecule = mol[0:i] + rep + mol[i+len(key):]
                            if new_molecule not in new_molecules:
                                new_molecule_tree.append(new_molecule)
                                print(new_molecule)
    molecule_tree = new_molecule_tree

print("Medicine found in", generation, "steps")