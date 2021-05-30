"""how to find the index of each item"""

def exzip1():
    Numbers =[1,2,3,4,6,4,3,6,8,5,8]

    #problem this will give only index for first 6 if you have duplicates in list.
    #print(Numbers.index(6))

    """finding index of all elements even with duplicates"""
    #an enumerator provides an index of each elements in list or iterables and return an output in the form of tuple.
    #syntax: enumerte(iterables,start=0) # it return iterable object

    for i in enumerate(Numbers,start=5):
        print("Index of {} is {}".format(i[1],i[0]))

    #find out all indexes of single element.
    for i in enumerate(Numbers):
        if i[1]==8:
            print("Index of {} is {}".format(i[1],i[0]))

    #print(list(enumerate(Numbers)))


def enumOverDict():
    Alphabets ={"AA": 4,"BB":9,"C":16,"DD":25,"EE":36}

    for i,j in enumerate(Alphabets):
        print(i,j)

def zipUsed():
    """zip function takes iterables and these iterables can be zero or more."""
    #Zip function will combine them and return it in the form of tuple.

    result =zip()
    print(result)   # it will be the object.
    listResult = list(result)
    print(listResult) #it will create empty list

    nlist=[4,5]
    slst=['four','Five','Six','Seven']
    r_tup=('IV','V','VI','VII')

    result= zip(nlist,slst,r_tup)
    result2= zip(nlist,slst,r_tup)

    setResult = set(result)
    print(setResult)
    setResult2 = tuple(result2)
    print(setResult2)

    """problem zip stop when the shortest iterable is exhausted."""

def ex2Zip():
    pm=['modi','biden','jacinda','scott','boris']
    country= ['india','us','nz','aus','uk']

    for pm ,country in zip(pm,country):
        print("Prime Minister: %s Country is: %s" %(pm,country))

    #how to converts dict from these 2 lists.
    pm = ['modi', 'biden', 'jacinda', 'scott', 'boris']
    country = ['india', 'us', 'nz', 'aus', 'uk']
    print(dict(zip(pm,country)))
ex2Zip()