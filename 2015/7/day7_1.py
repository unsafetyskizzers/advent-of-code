input = open("input.txt", "r")

def int16(n):
    return int(n) % 65535

signals = {}
no_signals = 1
loops = 0

while no_signals > 0 and loops < 10000:
    no_signals = 0
    for line in input:
        command = line.strip().split()
        match len(command):
            case 3: # command with 3 parts must be a signal assignment
                if command[2] not in signals:
                    signals[command[2]] = int16(command[0])
            case 4: # command with 4 parts must be a NOT gate
                if command[1] in signals:
                    if command[3] not in signals:
                        signals[command[3]] = ~signals[command[1]]
                else:
                    no_signals += 1
            case 5: # command with 5 parts may be any other gate
                if command[1] == "AND":
                    if command[0] in signals and command[2] in signals:
                        if command[4] not in signals:
                            signals[command[4]] = signals[command[0]] & signals[command[2]]
                    else:
                        no_signal += 1
                elif command[1] == "OR":
                    if command[0] in signals and command[2] in signals:
                        if command[4] not in signals:
                            signals[command[4]] = signals[command[0]] | signals[command[2]]
                    else:
                        no_signal += 1
                elif command[1] == "LSHIFT":
                    if command[0] in signals:
                        if command[4] not in signals:
                            signals[command[4]] = signals[command[0]] << int(signals[command[2]])
                    else:
                        no_signal += 1
                elif command[1] == "RSHIFT":
                    if command[0] in signals:
                        if command[4] not in signals:
                            signals[command[4]] = signals[command[0]] >> int(signals[command[2]])
                    else:
                        no_signal += 1
    loops += 1

if loops == 10000:
    print("No solution after 10000 loops")
else:
    print("Signal of wire a:", signals["a"])
