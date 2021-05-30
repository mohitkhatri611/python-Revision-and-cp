"""  * to take in a variable number of arguments
we want to make a multiply function that takes any number of arguments
and able to multiply them all together. It can be done using *args.

Use : if you are note sure about how many arguments you are going to pass.
args means arbitrary number of arguments which means variable no. of args. in form of tuple

"""
"""Important: Remember *arg receive multiple arug as tuple 
                **kwargs receive multiple keyword arguments as dictionary form
"""

def myFun(*argv):
    for arg in argv:
        print(arg, end=' ')


def myFun1(arg1, *argv):
    print(arg1)
    for arg in argv:
        print(arg, end=' ')

#myFun1('Hello', 'Welcome', 'to', 'GeeksforGeeks')

""" **kwargs used to pass a keyworded, variable-length argument list
double star allows us to pass through keyword arguments (and any number of them)
     A keyword argument is where you provide a name to the variable as you pass it into the function
     can think of the kwargs as being a dictionary that maps each keyword to the value that we pass alongside it.
      That is why when we iterate over the kwargs there doesn’t seem to be any order in which they were printed out
      kwargs arguments should be unique otherwise error.
"""

def myFun3(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s"%(key,value))

#myFun3(first="geeks",mid='for', last='Geeks',last='Geeks') #Error as we can't repeast keyword args
#myFun3(first="geeks",mid='for', last='Geeks')

def myFun4(arg1, **kwargs):
    #arg and kwargs
    for key, value in kwargs.items():
        print ("%s == %s" %(key, value))
#myFun("Hi", first ='Geeks', mid ='for', last='Geeks')


"""Using *args and **kwargs to call a function"""


def myFun5(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

# args = ("Geeks", "for", "Geeks")
# myFun5(*args)
#
# kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
# myFun5(**kwargs)

"""Using *args and **kwargs in same line to call a function, use both at one time """

def myFun6(*args, **kwargs):
    print(type(args))
    print("args: ", args)
    print("kwargs ", kwargs)

#myFun('geeks','for','geeks',first="Geeks",mid="for",last="Geeks")


def test(*args):
    print("args", args)
    print("type: ", type(args))
    print("Sum:", sum(args))  #to sum of all the args

#test(1,1,2,3,4)

def is_even(*args):
    even_list = [num for num in args if num% 2==0]
    return even_list

#print(is_even(12,33,53,64,25,754,2,6))
#print(is_even(12,33,53,64,25,754,2,6))

def student_info(**kwargs):
    print(f"Name: {kwargs['name']} \tEnroll: {kwargs['enroll']}")


# student_info(name="Deniel", age= 19, enroll= "Python")
# student_info(name="Mark", enroll="java")

def total_sales(*p,**r):
    total = sum(p)
    print(f"{r['day']} sales: {total}")

# total_sales(45,45,day="Monday")
# total_sales(100,200,300,day="Friday")

def total_sales(brand_name,*args,**kwargs):
    total = sum(args)
    print(f"{kwargs['day']} sales: {total} of {brand_name}")

total_sales('Puma', 100,500, day="Wednesday")
total_sales("Nike",1500,1600,day="Friday")




