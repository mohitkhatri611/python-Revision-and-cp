def shsort(myarray, n):
    g = n//2  # dividing the number of elements by 2 to find the gap
    while g > 0:
        for x in range(g,n):
            y=myarray[x]
            z=x
            while z >=g and myarray[z-g] > Y:
                myarray[z] = myarray [z-g]
                z-=g
            myarray[z]=y
        g//=2

mylist=[23,12,1,17,45,2,13]
lenght =len(mylist)
shsort(mylist, lenght)
shsort(mylist, length)
print(mylist)