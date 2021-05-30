"""finding  Index of Non-Zero elements in Python list using enum and list comprehension"""


def prog():
    test_list = [6, 7, 0, 1, 0, 2, 0, 12]
    print("original list: ",test_list)

    #index of non- zero elements in python list
    #using list comprehension and enumeration.

    res =   [idx for idx,val in enumerate(test_list) if val!=0]

    print("Indexes are: ", res)

prog()
