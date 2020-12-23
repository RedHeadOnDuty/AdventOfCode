
Input = open("input.txt").read().split("\n")

accumulator = 0


commands = []
amount = []
for line in Input[:-1]:
    temp = line.split(" ")
    commands.append(temp[0])
    amount.append(temp[1])


def test(cmd):
    global accumulator
    accumulator = 0
    i = 0
    watchList = []
    while True:
        if i in watchList:
            return False
        if i == len(commands):
            return True
        print(cmd[i], amount[i])
        watchList.append(i)
        if cmd[i] == "acc":
            accumulator += int(amount[i])
            i += 1
        elif cmd[i] == "jmp":
            i += int(amount[i])
        elif cmd[i] == "nop":
            i += 1


def test2():
    i = 0
    while True:
        cmd = commands
        if cmd[i] == "acc":
            i += 1
            continue
        elif cmd[i] == "jmp":
            cmd[i] = "nop"
        elif cmd == "nop":
            cmd[i] = "jmp"
        if test(cmd):
            break
        i += 1

    print(accumulator)


test2()
