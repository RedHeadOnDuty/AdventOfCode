def Day2_0():
    Paswoerter = open('C:\\Users\Christopher K\PycharmProjects\AdventOfCode/Days/Input/inputD2.txt').readlines()
    return Paswoerter

def  add_Dictionarie_Item(line):
    Dictionarie_Item = {}
    Line_Split = line.split()
    MinMax_Split = Line_Split[0].split("-")
    Dictionarie_Item["min"] = MinMax_Split[0]
    Dictionarie_Item["max"] = MinMax_Split[1]
    Dictionarie_Item["key"] = Line_Split[1][0]
    Dictionarie_Item["password"] = Line_Split[2]
    return Dictionarie_Item

def Day2_1():
    Number_of_is_Valid = 0
    List = []
    i = 0

    for line in List:
        Anzahl_key = (List[i]["password"].count(List[i]["key"]))
        if Anzahl_key > int(List[i]["max"]) or Anzahl_key < int(List[i]["min"]):
            pass
        else:
            Number_of_is_Valid += 1
        i += 1

    print(Number_of_is_Valid)
    return "//finished//"


def Day2_2():
    Number_of_is_Valid = 0
    List = []
    for line in Day2_0():
        List.append(add_Dictionarie_Item(line))
    for line in List:
        temp1 = line["password"][int(line["min"]) - 1]
        temp2 = line["password"][int(line["max"]) - 1]
        if ((line["key"] == temp1) or (line["key"] == temp2)) and (not temp1 == temp2):
            Number_of_is_Valid += 1
    print(Number_of_is_Valid)
    return "//finished//"


def Lars():
    rows = Day2_0()
    correct = 0
    for row in rows:
        cond, pwd = row.split(": ")
        nums, char = cond.split()
        n1, n2 = nums.split("-")
        n1 = int(n1)
        n2 = int(n2)
        if (pwd[n1-1] == char and pwd[n2-1] != char) or (pwd[n1-1] != char and pwd[n2-1] == char):
            correct += 1
    print(correct)
    return "//finished"
