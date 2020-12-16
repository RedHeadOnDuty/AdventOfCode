from Days.Input.ReadInput import Input


def Day5_1():
    PassengerList = Input("C:\\Users\Christopher K\PycharmProjects\AdventOfCode/Days/Input/inputD5.txt")

    for i in range(len(PassengerList)):
        PassengerList[i] = list(PassengerList[i].strip("\n"))
        for j in range(len(PassengerList[i])):
            if PassengerList[i][j] == "F":
                PassengerList[i][j] = 0
            elif PassengerList[i][j] == "B":
                PassengerList[i][j] = 1
            elif PassengerList[i][j] == "R":
                PassengerList[i][j] = 0
            elif PassengerList[i][j] == "L":
                PassengerList[i][j] = 1
        s = [str(k) for k in PassengerList[i]]
        res = format(int("".join(s), 2), '010b')
        PassengerList[i] = res

    # print(MaxID(max(PassengerList)))
    print(Aufgabe2(sorted(PassengerList)))

    return "//finished//"


def MaxID(MaxID):
    highest = MaxID
    temp = int(str(highest)[:-3], 2) * 8 + int(str(highest)[-3:], 2)
    return temp


def Aufgabe2(PassengerList):
    tempO = 13
    for i in range(8, len(PassengerList)):
        print(int(PassengerList[i], 2))
        tempN = int(str(PassengerList[i])[:-3], 2) * 8 + int(str(PassengerList[i])[-3:], 2)
        if not tempN == tempO + 1: # and tempN != 651:
            break
        tempO = tempN

    return "\n" + str(tempO + 1)
