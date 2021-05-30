"""
map() function returns a map object(which is an iterator)
of the results after applying the given function to each item of a given iterable (list, tuple etc.)

syntax: map(fun, iterrables)
map(fun, iterable1,iterable2,.... iterableN)
fun can be normal function or lambda function.
You can pass one or more iterable to the map() function.
"""
def power(n):
    return n*n
def ex1():
    x=map(power, [1,2,3,4,5])
    #print(x)
    print(list(map(power, [1,2,3,4,5])))
    #print(tuple(x))
    print(set(x))

def power2(n,m):
    return n*m

def ex2():
    x=map(power2,[1,2,3,4,5],[2,3,2,2,2])
    print(list(x))

def exlambda():
    l=map(lambda x,y: x*y,[1,2,3,4,5],[5,5,3,4,5])
    print(list(l))
    #carefull your args and expressions should be same length other wise error
    print(list(map(lambda x,y,z: x*y*z,[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5])))

def exstring():
    string = "Hello friends how are your?"
    print(list(map(lambda x: len(x),string.split())))
    #output[5, 7, 3, 3, 5]

"""filter() function, random and list compression"""
def Result(n):
    if n>50:
        return n

def exrandom():
    import random
    num= [random.randint(10,100) for i in range(20)]
    print(num)
    #printing numbers which are greater than 50.
    print(list(filter(Result,num)))

"""...Syntax : filter(function or None, iterable)-->filter object"""

def exfilter2():

    mixedData= [34,57,31,False,35,"hi","",34,67,0,[],{}]
    filtered_Data = filter(None, mixedData)
    #this will skip blank data, false values and blank strings or empty brackets
    print(list(filtered_Data))

def exFilterLambda():
    """using filter with lambda"""
    import random
    print(list(filter(lambda x: x>=50 and x<=80,[random.randint(10,100) for i in range(20)])))
def exFilter2():
    ai="""Artificial intelligence (AI) is intelligence demonstrated by machines, unlike the natural intelligence displayed by humans and animals, which involves consciousness and emotionality. The distinction between the former and the latter categories is often revealed by the acronym chosen. 'Strong' AI is usually labelled as artificial general intelligence (AGI) while attempts to emulate 'natural' intelligence have been called artificial biological intelligence (ABI). Leading AI textbooks define the field as the study of "intelligent agents": any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals.[3] Colloquially, the term "artificial intelligence" is often used to describe machines that mimic "cognitive" functions that humans associate with the human mind, such as "learning" and "problem solving"."""
    print(list(filter(lambda x: len(x)>10, ai.split())))
    #que? -> now filter those word which haveing either x or p albpha in your ai string.


"""reduce function with map"""
import random
from functools import reduce
def exReduce1():

    print(reduce(lambda a,b: a+b,[1,2,3,4,5]))

    print(reduce(lambda x,y: x*y, range(1,5)))

    #Ex with random filter and map and lambda.

    num = [random.randint(10, 100) for i in range(20)]
    print(list(filter(lambda x: x<=40,num)))
    print(list(map(lambda x: x+x,filter(lambda x: x<=40,num))))
    #here we filter those value which are less than 40 and after that we pass them
    #after that those value i am going to pass to the map function.
    """now try to reverse the order of above """
    print(list(filter(lambda x: x>=40, map(lambda x: x+ x, num))))

def exReduce2():
    num = [random.randint(10, 100) for i in range(20)]
    #reduce syntax reduce(fun, iterables)
    print(reduce(lambda x,y: x+y,map(lambda x: x+x, filter(lambda x:  x>=20 and x<=50, num))))


def strReduce1():
    """Reduce the tuple to 1 single string or concate elements"""
    str_list= ("This", "is", "string", "concat", "by", "reduce")
    print(reduce(lambda x,y: x+" " +y,str_list))
    #output This is string concat by reduce


def addNumbersList():
    numbers1 = [1, 2, 3]
    numbers2 = [4, 5, 6]
    result = map(lambda x, y: x + y, numbers1, numbers2)
    print(list(result))

def listofStrings():
    l=['sat','bat','cat','mat']
    test=map(list,l)
    print(list(test))
    #output : [['s', 'a', 't'], ['b', 'a', 't'], ['c', 'a', 't'], ['m', 'a', 't']]
listofStrings()