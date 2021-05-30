"""Check whether two strings are anagram of each other"""
"Method 1 mine"
class Solution:
    # Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self, a, b):
        # code here
        from collections import Counter

        if Counter(a) == Counter(b):
            return True
        else:
            return False

"Method 2 sorted string and check if equal"

def sortStr(str1, str2):
    #Time Complexity: O(nLogn)
    str1=sorted(str1)
    str2= sorted(str2)
    #print(str1, str2)
    if str1==str2:
        return True
    else:
        return False

print(sortStr("mohit","mhoit"))

""" #Method 3 using the Count characters using array 

NO_OF_CHARS = 256
def areAnagram(str1, str2):
    # Create two count arrays and initialize all values as 0
    count1 = [0] * NO_OF_CHARS
    count2 = [0] * NO_OF_CHARS
    #observe the initialize of arrays to 0
    for i in str1:
        count1[ord(i)] += 1

    for i in str2:
        count2[ord(i)] += 1


    if len(str1) != len(str2):
        return 0

        # Compare count arrays
    for i in range(NO_OF_CHARS):
        if count1[i] != count2[i]:
            return 0

    return 1


str1 = "geeksforgeeks"
str2 = "forgeeksgeeks"

if areAnagram(str1, str2):
    print("yes")
else:
    print ("No")
"""

"""Method 4 ->count characters using one array"""