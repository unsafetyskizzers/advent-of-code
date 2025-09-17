input = open("2015/7/input.txt", "r")

def int16(n):
    return int(n) & 0b1111111111111111

signals = {}

def get_signal(sig):
    if sig.isdigit():
        return int16(sig)
    elif sig in signals:
        return signals[sig]
    else:
        return -1

command_stack = []
for line in input:
    command_stack.append(line.strip().split())

loops = 0

while command_stack != [] and loops < 10000:
    for command in command_stack:
        match len(command):
            case 3: # command with 3 parts must be a signal assignment
                if get_signal(command[0]) > -1:
                    signals[command[2]] = get_signal(command[0])
                    command_stack.remove(command)
            case 4: # command with 4 parts must be a NOT gate
                if get_signal(command[1]) > -1:
                    signals[command[3]] = int16(~int16(get_signal(command[1])))
                    command_stack.remove(command)
            case 5: # command with 5 parts may be any other gate
                if get_signal(command[0]) > -1 and get_signal(command[2]) > -1:
                    if command[1] == "AND":
                        signals[command[4]] = get_signal(command[0]) & get_signal(command[2])
                    elif command[1] == "OR":
                        signals[command[4]] = get_signal(command[0]) | get_signal(command[2])
                    elif command[1] == "LSHIFT":
                        signals[command[4]] = get_signal(command[0]) << int(command[2])
                    elif command[1] == "RSHIFT":
                        signals[command[4]] = get_signal(command[0]) >> int(command[2])
                    command_stack.remove(command)
    print(command_stack)
    loops += 1

if loops >= 10000:
    print("No solution after 10000 loops")
else:
    print("Signal of wire a:", signals["a"], "after", loops, "loops")
