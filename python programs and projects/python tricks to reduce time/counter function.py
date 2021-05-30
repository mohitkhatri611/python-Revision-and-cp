def isAnagram(self, a, b):
    # code here
    from collections import Counter

    if Counter(a) == Counter(b):
        return True
    else:
        return False


""" infinite for loop"""
import itertools
for i in itertools.count():
    print(i)

x="global variable"

def test_life():
    global x    #using this we access the global variable otherwise locally x will be created newly.
    x="local variable"
    print(x)