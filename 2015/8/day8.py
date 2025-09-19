input = open("2015/8/input.txt", "r")
lines = input.readlines()
input.close()

for i in range(len(lines)):
    lines[i] = lines[i].strip()

code_chars = 0
str_chars = 0
diff_chars = 0

for line in lines:
    skip_chars = 0
    code_chars += len(line)
    for i in range(len(line)):
        if skip_chars == 0:
            if line[i] == "\\":
                if line[i+1] == "\\" or line[i+1] == "\"":
                    skip_chars = 1
                elif line[i+1] == "x":
                    skip_chars = 3
            str_chars += 1
        else:
            skip_chars -= 1
    str_chars -= 2 # remove quotes
print("Difference (part 1):", code_chars - str_chars)

new_lines_chars = 0

for line in lines:
    new_line = r""
    for i in range(len(line)):
        if line[i] == "\\":
            new_line += r"\\"
        elif line[i] == "\"":
            new_line += r"\""
        else:
            new_line += line[i]
    new_lines_chars += len(new_line)
    new_lines_chars += 2 # add quotes

print("Difference (part 2):", new_lines_chars - code_chars)