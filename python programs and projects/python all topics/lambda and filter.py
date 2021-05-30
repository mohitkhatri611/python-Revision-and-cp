"""
The filter() function in Python takes in a function and a list as arguments. This offers an elegant way to filter out all the elements of a sequence “sequence”, for which the function returns True

"""

def ex1():
    my_list = [12, 65, 54, 39, 102, 339, 221, 50, 70, ]

    # use anonymous function to filter and comparing
    # if divisible or not

    result= list(filter(lambda x: (x%13==0),my_list))
    print(result)

def ex2():
    """ find all Palindromes."""
    my_list = ["geeks", "geeg", "keek", "practice", "aa"]

    result= list(filter(lambda x: (x=="".join(reversed(x))),my_list))
    print(result)

    """find all anagrams of str in"""
    from collections import Counter
    my_list = ["geeks", "geeg", "keegs", "practice", "aa"]
    str = "eegsk"
    #use anonymous function to filter anagrams of x.
    """An anagram of a string is another string that contains same characters, only the order of        characters can be different. For example, “abcd” and “dabc” are anagram of each other"""

    result= list(filter(lambda x: (Counter(str)==Counter(x)),my_list))
    print(result)



"""Count frequencies of all elements in array in Python using collections module """

# Function to count frequency of each element
import collections

# it returns a dictionary data structure whose
# keys are array elements and values are their
# corresponding frequencies {1: 4, 2: 4, 3: 2,
# 5: 2, 4: 1}
def CountFrequency(arr):
    return collections.Counter(arr)


# Driver function
if __name__ == "__main__":

    arr = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 5, 5]
    freq = CountFrequency(arr)

    # iterate dictionary named as freq to print
    # count of each element
    for (key, value) in freq.items():
        print(key, " -> ", value)


""" Function to find intersection of two arrays"""

def interSection():
    arr1 = [1, 3, 4, 5, 7]
    arr2 = [2, 3, 5, 6]
    # filter(lambda x: x in arr1, arr2)  -->
    # filter element x from list arr2 where x
    # also lies in arr1
    result = list(filter(lambda x: x in arr1, arr2))
    print("Intersection : ", result)




