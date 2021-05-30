"""https://www.youtube.com/watch?v=C-gEQdGVXbk&ab_channel=CoreySchafer"""

#1. use ternary operators.
def ex():
    condition=True
    if condition:
        x=1
    else:
        x=0
    #better code would be ternary for single line.
    x=1 if condition else 0

    #ex2................................................................
    num1=10000000000
    num2=10_000_0000 #doesn't effect and easy to read.
    total=num1+num2
    print(f'{total:,}')
    #10,100,000,000 output will be with comas using format string.
    #use underscore to seperate this will not effect number

def ex2():
    #use context manager to open fine it will automatically close when data read or write........
    #got completed.
    with open('test.txt','r') as f:
        file_content = f.read()
    words= file_content.split('')
    word_count=len(words)
    print(word_count)

    #IT automatically manage resource for you. you can use it while db connection, xml files or etc.
    #called context manager

def ex3():
    names =['corey', 'charis', 'dave','travis']
    index =0
    for name in names:
        print(index, name)
        index +=1

    #better way to keep track of index...
    for index,name in enumerate(names): #by default if not specified it start wiht 0
        print(index,name)
    for index,name in enumerate(names, start=1):
        print(index,name)
def ex4():
    #loop over 2 list
    names = ['corey', 'charis', 'dave', 'travis']
    heroes=['spider man','superman','deadpool','batman']
    universe=['marave','dc','maravel','dc']
    for index, name in enumerate(names):     #not better code.
        hero=heroes[index]
        print(f'{name} is actually {hero}')

    #now better code. use zip it allows you to loop over 2 lists at once and again it return both values at once.

    for name, hero,universe in zip(names,heroes, universe):
        print(f'{name} is actually {hero} from {universe}')

    #here zip is returning a tuple of 3 items here, and we are just unpacking them just by setting
    #3 different variables. We can access the single tuple if we wanted.

    for value in zip(names,heroes, universe):
        print(value)
    #zip will stop after the shortest list is exhausted.
    #if you want zip to go to the end of the longest list then you have to use the zip longest function.
    # from the itertools library

def exUnpacking():
    #unpacking
    #a,b=(1,2)
    #you can use _ as convention that we are planning to not use that varialbe anywhere in code.................
    #a,b,c=(1,2) #this will give you an error.............not enough value to unpack.
    a,b,*c = (1,2,3,4,5) # this * will make set rest of values to c we can use this in lists it store other value in list.
    #a, b, *_ = (1, 2, 3, 4, 5) #if you plan to not to use variable.
    print(a)
    print(b)
    print(c)
    #output
    """ 1
        2
        [3, 4, 5]"""
    a, b, *c,d = (1, 2, 3, 4, 5,6,7) #this will make d value to last value set.

def ex5Class():
    #for getting and setting attributes on a certain object..........
    class Person():
        pass
    #way 1.
    # person = Person()
    # person.first = "Corey"
    # person.last="Schafer"
    #
    # print(person.first,person.last)

    #way 2.........
    #setattr(person,'first','corey') #using string directly.

    #setting using variable........
    person=Person()
    first_key ="first"
    first_val ='Corey'
    setattr(person,first_key,first_val)
    first = getattr(person, first_key)
    #print(first)

    #................................................................
    #now looping over it
    person= Person()
    person_info= {'first':'corey','last': 'Schafer'}
    for key, value in person_info.items():
        setattr(person,key,value)

    for key in person_info.keys():
        print(getattr(person,key))

def exSecretInfo():
    #built in function for password.
    #don't want to write password seen to on screen to see every one.
    from getpass import getpass
    username = input('Username:')
    password = getpass('Password:')
    #but here in this one proble it is going over loop you can rectivfy it
    print('Logging In...',username,password)

    """
    python -m venv envname #using -m we are importing module it sill serach that module from directories.
    and you don't need to specify the .py extension also.
    
    """
    help(getpass)   #show the doc and various functino we can use them

    from datetime import datetime
    dir(datetime) #only show attributes and method that are available.
    

exSecretInfo()