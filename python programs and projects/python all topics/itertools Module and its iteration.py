#import itertools
from itertools import *

number=[7,2,6,3,5,9,4,10,8,7,12,15]

def ex1():
    # print(dir(itertools)) #show all the avl functions
    #accumulate means running total 7,7+2, 7+2+6, 7+2+6+3,.... until end of list
    for i in accumulate(number):
        print(i, end=" ")
    #output is: 7 9 15 18 23 32 36 46 54 61 73 88

    #count is infinite iterator syntax: count(start, stepsize, stop)
    #can be infinite
    # for i in itertools.count():   #tthis is infinite for loop
    #     print(i)
    for i in count(10,2):
        if i==30:
            break
        else:
            print(i, end=' ')
    #output: 10 12 14 16 18 20 22 24 26 28
    """ cycle: it elements form the iterable until it is exhausted. Then repeat the sequence indefinitely."""
    print()
    j=0
    for i in cycle("321"):    #"this is also infintie iterator"
        if j >15:
            break
        else:
            print(i,end=' ')
            j=j+1
    #output: 3 2 1 3 2 1 3 2 1 3 2 1 3 2 1 3

def ex2():
    """want to repeast something without looping concept"""

    print(list(repeat("python", 5)))

"""   Combinatoric Iterator like product, purmutation, combination etc."""

def exProduct():

    print("the cartesain product: ")
    print(list(product("ABC",[1,2,3])))
    #out: [('A', 1), ('A', 2), ('A', 3), ('B', 1), ('B', 2), ('B', 3), ('C', 1), ('C', 2), ('C', 3)]

    print(list(product(["A","B","C"],range(2))))
    #output: [('A', 0), ('A', 1), ('B', 0), ('B', 1), ('C', 0), ('C', 1)]

    """use list of list"""
    num= [[7,8,9],[4,5,6]]
    print(list(product(*num)))  # it is *arg so we can pass any number of list


def exPermutations():
    print(list(permutations("XYZ",2)))
    #output: [('X', 'Y'), ('X', 'Z'), ('Y', 'X'), ('Y', 'Z'), ('Z', 'X'), ('Z', 'Y')]

    print(list(permutations(range(1,4),3)))
    #[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

    for i in permutations(["A","B","C"]):
        print(i, end=" ")
    #output ('A', 'B', 'C') ('A', 'C', 'B') ('B', 'A', 'C') ('B', 'C', 'A') ('C', 'A', 'B') ('C', 'B', 'A')


def exCombination():

    print(list(combinations("ABC",2)))
    #output:[('A', 'B'), ('A', 'C'), ('B', 'C')]  # observer combination will have less combinations.

    #combination with replacement.
    print(list(combinations_with_replacement("123",2)))
    #here individual elements have successive repeats remember it when using it.
    #output: [('1', '1'), ('1', '2'), ('1', '3'), ('2', '2'), ('2', '3'), ('3', '3')]

    """generate combination of 3 digit those 3 digits could be anything but each combination result in
    sum should be there
    """
    #lst= [1,2,3,4,5,6]
    lst=[0,1,1,2]
    print([result for result in combinations(lst,3) if sum (result)==10]) #it will give without rearrangements
    print([result for result in permutations(lst, 3) if sum(result) != 3]) #it will give there rearrangements also so more are there

    X = int(input())
    Y = int(input())
    Z = int(input())
    N = int(input())
    print([[x, y, z] for x in range(X + 1) for y in range(Y + 1) for z in range(Z + 1) if x + y + z != N])
    #OUTPUT:[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]] #meand if input is 1,1,1,2 then print all permutation,
    #whose sum !=3.
    #other way.
    X, Y, Z, N = 1, 1, 1, 2
    from itertools import product
    [list(i) for i in product(range(X + 1), range(Y + 1), range(Z + 1)) if sum(i) != N]

exCombination()
def exOther():
    x=[1,2,3,4,5]
    y=["A","B","C"]

    print(list(zip_longest(x,y)))
    #this will continue until the longest iterable is exhausted and fill the default value when shortest arg. exhausted.
    #Output:  [(1, 'A'), (2, 'B'), (3, 'C'), (4, None), (5, None)]

    print(list(zip_longest(x,y,fillvalue="X")))
    #Output: [(1, 'A'), (2, 'B'), (3, 'C'), (4, 'X'), (5, 'X')]

    num=[7,2,6,3,5,9,4,10,12,15]
    #syntax: islice(iterable,start,stop[, step]) # it is just the slicing of list concept
    part_number= islice(number,4)
    for i in  part_number:
        print(i, end=" ")

    print()
    part_number = islice(number, 2,11,2)
    for i in  part_number:
        print(i, end=" ")


def exOther2():
    import operator
    #starmap is just power function like 3 to the power 4 i.e
    lst= [(3,4), (2,3),(4,3)]
    x = starmap(operator.pow,lst)
    for i in x:
        print(i, end=" ")


exOther2()