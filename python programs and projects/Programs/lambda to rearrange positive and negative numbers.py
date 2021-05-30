

def Rearrange(arr):

    return [ x for x in arr if x< 0] + [x for x in arr if x>=0]

if __name__=="__main__":
    arr=[12,11,-13,5,6,7,-3,5,-3,-6]

    print(Rearrange(arr))