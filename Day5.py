from Days.Input.ReadInput import Input

global PassengerList
PassengerList = Input("C:\\Users\Christopher K\PycharmProjects\AdventOfCode/Days/Input/inputD5.txt")

for i in range(len(PassengerList)):
    PassengerList[i] = list(PassengerList[i].strip("\n"))
    for j in range(len(PassengerList[i])):
        if PassengerList[i][j] == "F":
            PassengerList[i][j] = 0
        elif PassengerList[i][j] == "B":
            PassengerList[i][j] = 1
        elif PassengerList[i][j] == "L":
            PassengerList[i][j] = 0
        elif PassengerList[i][j] == "R":
            PassengerList[i][j] = 1
    s = [str(k) for k in PassengerList[i]]
    res = format(int("".join(s), 2), '010b')
    PassengerList[i] = res
PassengerList.sort()


def MaxID():
    highest = (str(max(PassengerList)))
    temp = int(highest, 2)
    return temp


def D5Aufgabe2():
    tempO = None
    for i in range(0, len(PassengerList)):
        # print(int(PassengerList[i][:-3], 2))
        # print(int(PassengerList[i][-3:], 2))
        tempN = int(PassengerList[i], 2)
        if 8 < tempN < MaxID() and not tempN == tempO + 1:  # 8 Sitze pro Reihe + Erste/Letzte Reihe unmöglich
            print(tempO, tempN)
            break
        print(tempO, tempN)
        tempO = tempN

    return "\n" + str(tempN - 1) + " " + str(MaxID())

