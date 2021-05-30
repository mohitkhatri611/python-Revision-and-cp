
def ex1():
    # Creating an empty dictionary
    myDict = {}

    # Adding list as value
    myDict["key1"] = [1, 2]
    myDict["key2"] = ["Geeks", "For", "Geeks"]

    print(myDict)

def ex2():
    # Creating an empty dictionary
    myDict = {}

    # Adding list as value
    myDict["key1"] = [1, 2]

    # creating a list
    lst = ['Geeks', 'For', 'Geeks']

    # Adding this list as sublist in myDict
    myDict["key1"].append(lst)

    print(myDict)

def ex3():
    myDict = dict()

    # Creating a list
    valList = ['1', '2', '3']

    # Iterating the elements in list
    for val in valList:
        for ele in range(int(val), int(val) + 2):
            myDict.setdefault(ele, []).append(val)
    print(myDict)

def ex4():
    #d= dict((val, range(int(val),int(val) + 2)) for val in ['1','2','3'])
    d =dict((val, range(int(val), int(val) + 2))
                        for val in ['1', '2', '3'])
    print(d)
    #outptut is wrong in this mentod.....carefull ......its output is not what is expected.


def ex5():
    #Using defaultdict

    from collections import defaultdict

    lst = [('Geeks', 1), ('For', 2), ('Geeks', 3)]
    orDict = defaultdict(list)

    # iterating over list of tuples
    for key, val in lst:
        orDict[key].append(val)

    print(orDict)
    #its output is not what is expected...

def ex6():
    #Using Json
    # importing json
    """very important here we are creating.... list of list as key  and single string as value"""
    import json

    # Initialisation of list
    lst = [('Geeks', 1), ('For', 2), ('Geeks', 3)]

    # Initialisation of dictionary
    dict = {}

    # using json.dump()
    hash = json.dumps(lst)

    # creating a hash
    dict[hash] = "converted"

    # Printing dictionary
    print(dict)
    #output: {'[["Geeks", 1], ["For", 2], ["Geeks", 3]]': 'converted'}

ex6()