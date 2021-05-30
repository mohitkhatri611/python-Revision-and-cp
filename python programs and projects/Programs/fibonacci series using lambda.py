

def ex1():
    from functools import reduce
    fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],
                           range(n-2), [0,1])

    #observe her fib is labmda function and we have named it. and we are apssing parameter to it.
    print(fib(5))

def ex2(count):
    #using lambda an dmap function
    fib_list= [0,1]
    any(map(lambda _: fib_list.append(sum(fib_list[-2:])),range(2,count)))
    #print(fib_list)
    return fib_list
print(ex2(10))