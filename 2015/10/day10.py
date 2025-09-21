file = open("2015/10/input.txt", "r")
orig_input = file.readlines()[0]
input = orig_input

print(input)

for i in range(40):
    newinput = ""
    char_copy_counter = 1
    char_copy = ""
    for ii in input:
        if ii != char_copy:
            if char_copy != "": newinput += str(char_copy_counter) + char_copy
            char_copy = ii
            char_copy_counter = 1
        else:
            char_copy_counter += 1
    newinput += str(char_copy_counter) + char_copy
    char_copy = ii
    char_copy_counter = 1
    input = newinput

print(input, "(length:", len(input), "after 40 loops)")

input = orig_input

for i in range(50):
    newinput = ""
    char_copy_counter = 1
    char_copy = ""
    for ii in input:
        if ii != char_copy:
            if char_copy != "": newinput += str(char_copy_counter) + char_copy
            char_copy = ii
            char_copy_counter = 1
        else:
            char_copy_counter += 1
    newinput += str(char_copy_counter) + char_copy
    char_copy = ii
    char_copy_counter = 1
    input = newinput
    print(input, "(length:", len(input), "after", i+1, "loops)")

print(input, "(length:", len(input), "after 50 loops)")