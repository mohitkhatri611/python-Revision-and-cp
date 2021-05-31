"""In greater details
keys wil be only single element.
value can be list or nested list or numbers, or other data str.
it is unorderd collection of items.
1. no duplicate keys is allowed.
2. value can be any type. while keys are immutable key numbers string or tuple.
3. Dict keys are case sensitive. Ex.
4. Keys in a dictionary doesn’t allows Polymorphism.
"""

def ex1():
    """emytp dictionary declare"""
    dct={}
    type(dict)

    dct1= dict() # define empty dict using constructor.
    type(dct1)

    #creating dict with list to tuples
    d= dict([(1,'abc'),(2,'xyz')])
    print(d)
    """access dict elements 2 ways:"""

    mydict={'name':"mohit", "age":25, 'mobile':[88888,9999]}
    #way 1
    # -1 would be last element of list 0,1,2,3...n, n-1..-3, -2, -1.
    print(mydict['age'], mydict['mobile'], mydict['mobile'][-1],mydict['mobile'][-2],mydict['mobile'][1])

    #other way...using get methood.
    print(mydict.get('name'),mydict.get('address'))
    """Note if any key which is accessed using get if is not there in dict then it will not through any error.
    but way 1st will throw error(keyError), if we use get then it will return None.
    
    """

def dictUpdate():
    d1= {'a':30, "b":40, "c":70}
    d2={'aa':'Abc','c':90,'B':100}
    d1.update(d2)
    print(d1)

    """other way to update"""
    d2.update(c=400,aa=10)
    print(d2)
    """how to add another key in your dict"""
    mydict = {'name': "mohit", "age": 25, 'mobile': [88888, 9999]}
    mydict['city']="Chennai"
    print(mydict)

def dictDel():
    """also remove elements"""
    mydict = {'name': "mohit", "age": 25, 'mobile': [88888, 9999]}
    #deleting element particulary is

    mydict.pop('age')

    #other way using popItem()
    # popitem() will remove key pair from your dict and return type is tuple.
    #it will delete item for right to left automatically whenever called.
    print(mydict)
    mydict.popitem()
    print(mydict)
    """clearing all the item from my dictionary."""

    mydict.clear()
    print(mydict)

def copydict():
    mydict = {'name': "mohit", "age": 25, 'mobile': [88888, 9999],'city':'Chennai'}
    d2=mydict.copy()
    print("d2",d2)

def addkey():
    mydict = {'name': "mohit", "age": 25, 'mobile': [8888, 9999], 'City': 'Chennai'}
    mydict.update(Address='242  sector ')
    print(mydict)
    """how to sort the list"""
    print(sorted(list(mydict.keys())))
    print(ord("A")) #printing the unicode of A i.e 65
    print(ord("a"))# 97 unicode

    print(sorted(mydict.get("mobile"),reverse=True))
    mydict.update(mobile= sorted(mydict.get("mobile"), reverse=True)) #saving reverse order to above dict.
    print(mydict)

def dictItem():
    mydict = {'name': "mohit", "age": 25, 'mobile': [8888, 9999], 'City': 'Chennai'}

    print(mydict.items())   #it will return the list of tuples.

    print(mydict.values()) # it will return the list of your values but return type is dict_values

    """how to check the presence of any key in the dict using the membership operator.
    means if any key is present or not.
    """
    print("add" in mydict)
    print("age" in mydict)

dictItem()
def dictDefault():
    """Dictionary setdefault()"""

    # syntax key-> > any key you want to return for
    # default-> > A value to insert if the specified key is not found. Default value is None

    d = {'name':'A','age':30}
    d.setdefault('add','E-101')
    d.setdefault('Grade')
    """this is default set to None if key is not present and if key is present then it return the value"""
    print(d)
    v=d.setdefault('name',"B")
    print(v)

def dictFromKeys():
    """ usiing from key method we can create a new dictionary with default value for all these keys
    if you not define the default value all the keys set to None value.
    In the fromkeys() you can define any iterables you can define list, you can define sets.
    """
    dct = dict.fromkeys(["english", "history","math"])
    print(dct)

    #you can also define default values for them
    dct = dict.fromkeys(["english", "history", "math"],0)
    print(dct)
    dct = dict.fromkeys(["english", "history", "math"],75)
    print(dct)

def clearAllItems():
    dct = dict.fromkeys(["english", "history", "math"])
    dct.clear()
    print(dct)

def listkeyAppend():
    myDict = {}

    # Adding list as value or single vale to key
    myDict["key1"] = [1, 2]
    # creating a list
    lst1=[2,"geeks","565"]
    lst = 6
    # Adding this list as sublist in myDict
    myDict["key1"].append(lst)
    myDict["key1"].append(lst1)
    print(myDict)

listkeyAppend()

from typing import List

#example of storing list as dictionary values.
def twoSum(nums, target):
    # Store indices into dictionary
    mydict = dict()
    for idx, num in enumerate(nums):
        if num in mydict.keys():
            mydict[num].append(idx)
        else:
            mydict[num] = [idx]

    for num in nums:
        # checks if target is a result of sum of same number residing in two different idx's
        if (target - num == num):
            if len(mydict.get(num)) >= 2:
                return mydict.get(num)[:2]
            continue

        # checks if target-num is in the dictionary
        elif mydict.get(target - num):
            return [mydict.get(num)[0], mydict.get(target - num)[0]]
    return None
print(twoSum([3,2,4],6))
print(twoSum([3,3],6))
