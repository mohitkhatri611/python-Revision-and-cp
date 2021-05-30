"""
    its an elegant way to define and create list based on your existing list
    it is generally more compact and faster compared to normal loops.
    But don't use it on long  comprehensions as its code is not user friendly.
    You can transfor any list comprehension to loop but not vice versa.
"""

def ex1():
    for i in  range(1,11):
        print(i,end=" ")

    #using comprehension
    print()
    print([i for i in range(1,11)])
    gen=(i for i in range(1, 11)) #so its is generator so we can iterate over it...
    for j in gen:
        print(j, end= " ")

    #other way you can use next(gen)
    print([i for i in dir(list)]) #shows the all functions that can be used with list include __ also.
    print([i for i in dir(list) if "__" not in i])  #shows function without underscore ..

def ex2():
    "square of each number"
    print([(i,i**2) for i in range(1,11) ])
    "even or odd numbers using this"
    print([num for num in range(2,20) if num % 2!=0])
    print([num for num in range(2, 20) if num % 2 == 0])

    "get power of num if that number is not completely divisible by "
    print([num if num%2==0 else num**2 for num in range(2,11)])

    "get number which is completely divisible by 3 or 9"
    print([num for num in range(1,100) if num%3 ==0 if num%9==0])

def ex3():
    "get the list for multiple of 20's "
    print([i * j for j in range(1, 11) for i in range(15, 21)])

    " without comprehese same thing"
    for i in range(15, 21):
        for j in range(1, 11):
            print(i * j, end=' ')
        print()
    # without comprehension flatter the given list.
    lst = [[1, 2, 3], [4, 5], [6, 7], [8, 9, 10]]
    # output should be [1,2,3,4,5,6,7,8,9,10]

    """without comprehension flatter the given list"""
    FlatternList = []
    for pair in lst:
        for ele in pair:
            FlatternList.append(ele)
    print(FlatternList)

    #using comprehension flattern the list
    print([ele for pair in lst for ele in pair])

    #other way
    print(sum(lst,[]))

def ex4():
    matrix =[[1,2],[3,4],[5,6],[7,8]]
    print([[pair[i] for pair in matrix] for i in range(2)]) #INTERESTING EXAMPLE
    #output: [[1, 3, 5, 7], [2, 4, 6, 8]]

    #pick any two char and make pair of combinations
    users= ["A","B","C","D"]
    pairs=[(x,y) for x in users for y in users if x!=y ]
    print(pairs)
    #output: [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'A'), ('B', 'C'), ('B', 'D'), ('C', 'A'), ('C', 'B'), ('C', 'D'), ('D', 'A'), ('D', 'B'), ('D', 'C')]
    pairs = [[x, y] for x in users for y in users if x != y] #outpt is list of list
    print(pairs)

    paragraph ="""Natural language processing (NLP) is a subfield of linguistics, computer science, and artificial intelligence concerned with the interactions between computers and human language,
     in particular how to program computers to process and analyze large amounts of natural language data.
     The result is a computer capable of "understanding" the contents of documents,
     including the contextual nuances of the language within them. The technology can then 
    accurately extract information and insights contained in the documents as well as categorize and organize the documents themselves"""

    print([word for word in paragraph.split() if len(word) < 5])

def ex5():
    #prime number using without list comprehension
    for i in range(2,50):
        for j in range(2,i):
            if i%j ==0:
                break
        else:
            print(i, end= " ")

    #Now with list comprehension
    print()
    #print([i for i in range(2,int(input("enter number: "))) if all (i%j !=0 for j in range(2,i))])
    print([i for i in range(2, 50) if all(i % j != 0 for j in range(2, i))])
    #all means
    lst=[6>5, 7<8, 10==11]
    all(lst) #if all elements are true then all return true and if any single is false then all returns false.

    for i in range(2,50):
        if all ([i%j !=0 for j in range(2,i)]):
            print(i, end= " ")

def exdictComprehension():
    #dictionary Comprehensions
    country = ["india","us", "nz"]
    pm= ["modi","Trump", "jacinda"]

    """we can map your 2 lists into the dictionary based on the comprehension"""
    my_dict = {country: pm for country, pm in zip(country, pm)}
    print(my_dict)
    #output: {'india': 'modi', 'us': 'Trump', 'nz': 'jacinda'}

    """how to generate the passwords"""

def genPasswords():
    import random, string
    string.printable

    print(["".join(random.choice(string.printable) for x in range(8,20))for i in range(5)])


genPasswords()



