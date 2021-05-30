def ex1():
    #Using map() + __add__
    test_list1 = [[1, 3], [4, 5], [5, 6]]
    test_list2 = [[7, 9], [3, 2], [3, 10]]

    # printing original lists
    print("The original list 1 is : " + str(test_list1))
    print("The original list 2 is : " + str(test_list2))

    # using map() + __add__
    # zipping lists of lists
    res = list(map(list.__add__, test_list1, test_list2))

    # printing result
    print("The modified zipped list is : " + str(res))

def ex2():
    # Using itertools.chain() + zip()
    import itertools

    # initializing lists
    test_list1 = [[1, 3], [4, 5], [5, 6]]
    test_list2 = [[7, 9], [3, 2], [3, 10]]

    # printing original lists
    print("The original list 1 is : " + str(test_list1))
    print("The original list 2 is : " + str(test_list2))

    # using map() + __add__
    # zipping lists of lists
    res = [list(itertools.chain(*i))
           for i in zip(test_list1, test_list2)]

    # printing result
    print("The modified zipped list is : " + str(res))