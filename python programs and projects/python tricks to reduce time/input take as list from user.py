
def ex1():
    lst = []
    for i in range(int(input())):
        ele= int(input())
        lst.append(ele)
    #this will take list in multiple lines single ele one by one.
    print(lst)

def ex2():
    # way 2.
    n = int(input())
    # this will take list as single line
    a = list(map(int, input().strip().split()))[:n]
    print("list", a)

def ex3():
    """list of list as input
    if input is like: Enter the number of elements: 3
            mohit
            23
            sagar
            4
            dsgf
            234
    """
    lst =[]
    n= int(input("Enter the number of elements: "))
    for i in range(0,n):
        ele = [input(),int(input())]
        lst.append(ele)
    print(lst)

def ex4():
    """using list comprehension and typecasting."""

    lst1=[] #for the list of integers
    lst2=[] #for the list of string / chars

    lst1=[int(item) for item in input("Enter the list item: ").split()]
    lst2 = [item for item in input("Enter the list item: ").split()]

    print(lst1,lst2)
    """
    Enter the list item: 23 34 25 62 62
    Enter the list item: mohit kahtri
    [23, 34, 25, 62, 62] ['mohit', 'kahtri']
    """


ex4()