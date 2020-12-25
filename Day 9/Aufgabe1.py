
Input = open("input.txt").read().split("\n")

global accumulator
accumulator = 0


command = []
amount = []
for line in Input[:-1]:
    temp = line.split(" ")
    command.append(temp[0])
    amount.append(temp[1])

i = 0
watchList = []
while True:
    if i in watchList:
        print(accumulator)
        print(i)
        break
    watchList.append(i)
    if command[i] == "acc":
        accumulator += int(amount[i])
        i += 1
    elif command[i] == "jmp":
        i += int(amount[i])
    elif command[i] == "nop":
        i += 1
