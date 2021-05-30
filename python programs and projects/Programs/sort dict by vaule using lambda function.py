"2 ways we can sort the dict 1. sorted with lambda 2. using itemgetter "
"""For descending order : Use “reverse = True” in addition to the sorted() function.
For sorting w.r.t multiple values: Separate by “comma” mentioning the correct order in which sorting has to be performed."""

"""use:  handling JSON data"""

def method1():
    # sorted() with lambda
    lis = [{"name": "Nandini", "age": 20},
           {"name": "Manjeet", "age": 20},
           {"name": "Nikhil", "age": 19}]

    #sorted by age
    print(sorted(lis,key= lambda i: i['age']))

    #sorted by both name and age if age is same then sorted by alphabet
    #but sorted by age
    print(sorted(lis, key=lambda i: (i['age'],i['name'])))

    #reverse order by
    print(sorted(lis,key=lambda i: i['age'],reverse=True))

from operator import itemgetter
def method2():
    # sorted() with lambda
    lis = [{"name": "Nandini", "age": 20},
           {"name": "Manjeet", "age": 20},
           {"name": "Nikhil", "age": 19}]

    #sorted by age
    print(sorted(lis, key=itemgetter('age')))

    print(sorted(lis,key=itemgetter('age','name')))

    print(sorted(lis,key=itemgetter('age'), reverse=True))
method1()