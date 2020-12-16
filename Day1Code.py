def Day1_0():
    Numbers = []
    with open('C:\\Users\Christopher K\PycharmProjects\AdventOfCode/Days/Input/input.txt') as f:
        Numbers.append(f.readlines())
    return Numbers


def Day1_1():
    Numbers = Day1_0()
    i2 = 0
    i1 = i2
    ListO = []

    for x in Numbers[0]:
        for y in Numbers[0]:
            if (int(Numbers[0][i1]) + int(Numbers[0][i2]) == 2020) and (x != y):
                test = True
                ListN = [int(Numbers[0][i1]), int(Numbers[0][i2])]
                for item in ListO:
                    if ListN == item:
                        test = False
                        break

                if test:
                    print(int(Numbers[0][i1]) * int(Numbers[0][i2]))
                    ListO.append(ListN)
            i2 += 1
        i2 = 0
        i1 += 1
    print(ListO)
    return "\n//finished//"


def Day1_2():
    Numbers = Day1_0()
    i2 = 0
    i1 = i2
    i3 = i2
    ListO = [0]
    test = True

    for x in Numbers[0]:
        for y in Numbers[0]:
            for z in Numbers[0]:
                if (int(Numbers[0][i1]) + int(Numbers[0][i2]) + int(Numbers[0][i3]) == 2020) \
                        and (x != y and x != z and y != z):

                    ListN = [int(Numbers[0][i1]), int(Numbers[0][i2])]

                    for item in ListO:
                        if ListN == item:
                            test = False
                            return test

                    if test:
                        print("hi")
                        print(int(Numbers[0][i1]) * int(Numbers[0][i2]) * int(Numbers[0][i3]))
                        ListO.append(ListN)
                i3 += 1
            i2 += 1
            i3 = 0
        i2 = 0
        i1 += 1
    return "\n//finished//"
