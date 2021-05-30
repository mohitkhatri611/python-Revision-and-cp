
def generator_functions():
    for i in range(5):
        yield i * 20
    #generator is a function normal function expect that it contains yield expression.
    #yield is a keyword in Python that is used to return from a function without destroying the states of its local
    # variable and when the function is called, the execution starts from the last yield statement.
    # Any function that contains a yield keyword is termed as generator. Hence, yield is what makes a generator.

    """ on large datasets generators are very usefull because generators are memory effiecible.
    # means generator function only store the previous result to generate the next sum. Instead of allocation of
    # memeory for all the result at the same time
    # In layman definition generators occupy less memory and very usefull for memory management."""

# 2 ways to access value of above function:
x= generator_functions()
#print(x)
#1 way
for item in x:
    print(item)


#2nd way:
y= generator_functions()
for i in range(5):
    print(next(y), end=' ')


#iteratable  are string, tuple, list, dict, but they are not iterators

a=[2,4,5,6,7]
#print(next(a))# will give error

b=iter(a)# converting to iterator
next(b)









