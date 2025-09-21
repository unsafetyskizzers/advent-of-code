import string

file = open("2015/11/input.txt", "r")
orig_input = file.readlines()[0].strip()
file.close()

alphabet = list(string.ascii_lowercase)

def increment_password(pword):
    if pword == "":
        return "a"
    elif pword[-1] == "z":
        return increment_password(pword[0:-1]) + "a"
    else:
        pword = pword[0:-1] + alphabet[alphabet.index(pword[-1]) + 1]
        return pword

def check_password(pword):
    pword_checklist = [0, 1, 0] # sequence, banned letters, pair
    last_pair_index = -4
    for i in range(len(pword)):
        if i < len(pword) - 2 and pword[i] not in ["y", "z"]:
            alpha_index = alphabet.index(pword[i])
            if pword[i+1] == alphabet[alpha_index + 1] and pword[i+2] == alphabet[alpha_index + 2]:
                pword_checklist[0] = 1
        if pword[i] in ["i", "o", "l"]:
            pword_checklist[1] = 0
        if i < len(pword) - 1:
            if pword[i] == pword[i+1] and i - 1 != last_pair_index:
                if last_pair_index == -4:
                    last_pair_index = i
                else:
                    pword_checklist[2] = 1
    if pword_checklist == [1, 1, 1]:
        return True
    else:
        return False

password = orig_input

while not check_password(password):
    password = increment_password(password)
    print("Incremented password to", password)

print("Final password:", password)