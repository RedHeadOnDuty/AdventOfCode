def Day3_0():
    Map = open('C:\\Users\Christopher K\PycharmProjects\AdventOfCode/Days/Input/inputD3.txt').readlines()
    i = 0
    for line in Map:
        Map[i] = line.strip()
        i += 1
    return Map

def Soso(Right, Down):
    Lines = Day3_0()
    trees = 0
    x2 = 0
    for i in range(0, len(Lines), Down):
        if Lines[i][x2] == "#":
            trees += 1
        x2 = (x2 + Right) % len(Lines[i])
    return trees


def Day3_1():
    List = [[3, 1]]

    Multiplie = Soso(List[0][0], List[0][1])
    print(Multiplie)

    return "//finished//"


def Day3_2():
    List = []
    List.append([1, 1])
    List.append([3, 1])
    List.append([5, 1])
    List.append([7, 1])
    List.append([1, 2])

    Multiplie = 1
    for item in List:
        Multiplie = Multiplie * Soso(item[0], item[1])
    print(Multiplie)

    return "//finished//"
