


def stringMethods():

        print("STRING METHODS \n")
        string = "helLO WoRlD"
        print(string.capitalize())
        print(string.casefold())
        print(string.center(20,"@"))
        print(string.count("o"))
        print(string.encode())
        print(string.endswith("D"))
        tabstring = "hello\tworld\thowareyou"
        print(tabstring.expandtabs(20))
        print(string.find("e"))
        print(string.format())
        print(string.isalnum())
        print(string.isalpha())
        print(string.isdecimal())
        print(string.isdigit())
        print(string.isidentifier())
        print(string.islower())
        print(string.isnumeric())
        print(string.isprintable())
        print(string.isspace())
        print(string.istitle())
        print(string.isupper())
        print(string.join("-"))
        print(string.lower())


def listMethods():
    print("------LIST-----")
    list = [1,2,232,"hello"]
    list2 = [1,2,232,"hello"]

    list.append("world")
    print(list)

    list2.clear()
    print(list2)

    list.copy()
    print(list)

    count = list.count(1)
    print(count)  
    
    list3 = [2,3,4,5,4,3,2,5,6]
    list.extend(list3)
    print(list)
    print()

    list.insert(5,'problem')
    print(list)

    list.pop(5)
    print(list)

    list.reverse()
    print(list)

    list3.sort()
    print(list3)

def setMethods():

    print('---SET---')

    set = {123,'hello',23,43,3,'world'}
    set.add('cat')
    print(set)

    set.copy()
    print(set)

    set.clear()
    print(set)

    set = {123,'hello',23,43,3,'world'}
    set2 = {32,54,3,23,134 ,'hello','world'}

    set3 = set.difference(set2)
    print(set3)

    set.difference_update(set2)
    print(set)

    set.discard(43)
    print(set)

    set3 = set.intersection(set2)
    print(set3)


def dictMethods():
    print("----DICT---")


while True:
    choice = input(" \n\n 1 STRING OPERATIONS \n 2 LIST OPERATIONS \n 3 SET OPERATIONS \n 4 DICT OPERATIONS")

    if int(choice) == 1:
        stringMethods()

    if int(choice) == 2:
        listMethods()

    if int(choice) == 3:
        setMethods()

    if int(choice) == 4:
        dictMethods()


