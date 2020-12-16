import string


def Read():
    input = open('C:\\Users\Christopher K\PycharmProjects\AdventOfCode/Days/Input/inputD4.txt').readlines()
    List = [[]]
    pruefListe = sorted(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])

    i = 0
    for line in input:
        if line == "\n":
            List.append([])
            i += 1
        else:
            List[i].append(line.strip())

    i = 0
    for item in List:
        List[i] = " ".join(item)
        i += 1

    List2 = []
    for Accounts in List:
        Dictionarie = {}
        Split = Accounts.split()
        for Splitter in Split:
            Split_ = list(Splitter.split(":"))
            Dictionarie[Split_[0]] = Split_[1]
        List2.append(Dictionarie)

    i = 0
    Pruefsumme = 0
    for item in List2:
        try:
            List[i] = item.pop("cid")
        except:
            pass
        i += 1
        for j in range(0, len(pruefListe), 1):
            if (len(list(item.keys()))) != len(pruefListe):
                break
            if test(item):
               break
            """
            print(sorted(list(item.keys()))[j])
            print(pruefListe[j])
            if sorted(list(item.keys()))[j] != pruefListe[j]:
                break
            """  # braucht man in dem fall nicht
            if j == len(pruefListe) - 1:
                Pruefsumme += 1

    print(Pruefsumme)
    return "//finised//"


def test(item) -> bool:
    if not 1920 <= int(item["byr"]) <= 2002:
        return True

    if not 2010 <= int(item["iyr"]) <= 2020:
        return True

    if not 2020 <= int(item["eyr"]) <= 2030:
        return True

    if item["hgt"].endswith("in"):
        if not (59 <= int(item["hgt"][:-2]) <= 76):
            return True
    elif item["hgt"].endswith("cm"):
        if not (150 <= int(item["hgt"][:-2]) <= 193):
            return True
    else:
        return True

    if not (item["hcl"].startswith("#") and len(item["hcl"]) == 7 and all(c in string.hexdigits for c in item["hcl"][1:])):
        return True

    if not item["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return True

    if not len(item["pid"]) == 9:
        return True

    return False
