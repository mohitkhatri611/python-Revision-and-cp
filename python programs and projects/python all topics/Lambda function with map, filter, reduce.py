#only single expression allowed to return after evaluation.
#can take any number of args.
"""
        Syntax: lambda arguments: expression
can be used along with built-in functions like filter(), map() and reduce().
lambda functino call anonymous function because it is define without name.
the expression returns automatically
"""
def ex1():
    print("printing list to given input like 123456...n")
    print("enter a number: ")
    list(map(lambda i: print(i, end=''), [i for i in range(1, int(input()) + 1)]))





def ex2():
    #printing in list
    print(list(i for i in range(1,10)))
    #output  [1, 2, 3, 4, 5, 6, 7, 8, 9]

def ex3():
    double = lambda x: x * 2
    print(double(6))

    num = lambda x: x + 5
    print(num(10))
    # two args for
    add = lambda x, y: x + y
    print(add(10, 20))

def ex4():
    lambda_cube= lambda y: y*y*y
    print(lambda_cube(10))


def ex5():
    #Using lambda() Function with filter()
    li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
    finla_list= list(filter(lambda x: (x%2!=0),li))
    #output: [5, 7, 97, 77, 23, 73, 61]
    print(finla_list)

    #Using lambda() Function with map()
    #to get double of a list.
    final_list= list(map(lambda x: x*2, li))
    print(final_list)

    animals = ['dog', 'cat', 'parrot', 'rabbit']
    #here we intend to change all animal names to upper case and return the
    upper_animal= list(map(lambda animal: str.upper(animal),animals))
    print(upper_animal)





def exReduce():
    """Using lambda() Function with reduce()
     reduce() function in Python takes in a function and a list as an argument. The function is called with a lambda    function and an iterable and a new reduced result is returned. This performs a repetitive operation over the        pairs of the iterable
     Here the results of previous two elements are added to the next element and this goes on till the end of the list like (((((5+8)+10)+20)+50)+100).
    """
    from functools import reduce
    li = [5, 8, 10, 20, 50, 100]
    sum= reduce((lambda x,y: x+y),li)
    print(sum)


    #ex2
    import functools
    lis = [1, 3, 5, 6, 2, ]
    print("The maximum element of the list is : ", end="")
    print(functools.reduce(lambda a,b: a if a>b else b, lis))


exReduce()