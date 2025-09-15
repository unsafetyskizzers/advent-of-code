code_file = open("code.txt", "r")
code_text = code_file.read()
code_file.close()
current_floor = 0
basement_index = -1

for i in range(len(code_text)):
    if code_text[i] == "(": current_floor += 1
    elif code_text[i] == ")": current_floor -= 1
    if current_floor < 0 and basement_index == -1: basement_index = i + 1
    
print("Floors travelled:", current_floor)
print("First basement visit:", basement_index)

input()