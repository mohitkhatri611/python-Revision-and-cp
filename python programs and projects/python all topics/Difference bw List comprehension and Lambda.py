"""
 define and create a list in python.
 We can create lists just like mathematical statements and in one line only. it consist of 3 parts.
1.Output expression,
2. Input sequence,
3. A variable representing a member of the input sequence and
4. An optional predicate part.

Syntax: List = [expression(i) for i in another_list if filter(i)]
Diff : List Comprehension is used to create lists,
Lambdas are functions that can process like other functions and thus return values or list.
"""

def ex1():
    lst = [x**2 for x in range(1,11) if x%2==1]
    print(lst)
    """
    In the above example,
        x ** 2 is the expression.
        range (1, 11) is input sequence or another list.
        x is the variable.
        if x % 2 == 1 is predicate part.
    """

def ex2():
    """lambda is anonymous function
    lambda arguments : expression
    """
    # Map basically iterates every element
    # in the list_ and returns the lambda
    # function result
    lst=list(map(lambda x: x**2, range(1,5)))
    print(lst)

    #other examples.
    x1 = (lambda x, y, z: (x + y) * z)(1, 2, 3)
    print(x1)

    # function using a lambda fumction
    x2 = (lambda x, y, z: (x + y) if (z == 0) else (x * y))(1, 2, 3)
    print(x2)

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    # using map() function
    squares = map(lambda x: x * x, nums)
    print(list(squares))

    # using filter() function
    evens = filter(lambda x: True if (x % 2 == 0)
    else False, nums)
    print(list(evens))

    d = (lambda x, y, z: x * y + z)(1, 2, 3)
    print(d)    #adding 1+2+3

ex1()
ex2()