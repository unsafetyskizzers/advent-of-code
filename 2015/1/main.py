code_file = open("code.txt", "r")
code_text = code_file.read()
current_floor = 0

for i in code_text:
    if i == "(": current_floor += 1
    elif i == ")": current_floor -= 1
    
print(current_floor)

input()