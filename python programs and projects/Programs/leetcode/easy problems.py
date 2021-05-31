import sys
from typing import List

#1848. Minimum Distance to the Target Element
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        res= sys.maxsize
        for i in range(len(nums)):
            if nums[i]==target:
                res= min(res,abs(i-start))
        return res

#1869. Longer Contiguous Segments of Ones than Zeros
def checkZeroOnes(s: str) -> bool:
    count0, count1, temp0, temp1 = 0, 0, 0, 0

    for number in s:
        if number == '0':
            temp0 += 1
            temp1 = 0
        else:
            temp1 += 1
            temp0 = 0
        count0 = max(count0, temp0)
        count1 = max(count1, temp1)

    return count1 > count0

print(checkZeroOnes("1101"))

#1. Two Sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #solution 1 using brute force O(n^2)
        for i, val in enumerate(nums):
            for k, val2 in enumerate(nums[i + 1:]):
                if (val + val2) == target:
                    print([i, i + 1 + k])
                    return [i, i + 1 + k]

        #solution 2  time-O(n)
        def twoSum(self, nums, target):
            cache = {}
            for idx, n in enumerate(nums):
                cv = cache.get(target - n)
                if cv != None and cv != idx:
                    return [cv, idx]
                cache[n] = idx
            return []

        # solution 3  time-O(n)
        nums_hash = {}
        for i, num in enumerate(nums):
            potentialMatch = target - num
            if potentialMatch in nums_hash:
                return [nums_hash[potentialMatch], i]
            nums_hash[num] = i

        # solution 4  time-O(n)
        hash_table = {}
        for i in range(len(nums)):
            if nums[i] in hash_table:
                return [hash_table[nums[i]], i]
            else:
                hash_table[target - nums[i]] = i

        #solution 5 time O(n)
        # Store indices into dictionary in list of indices.
        mydict = dict()
        for idx, num in enumerate(nums):
            if num in mydict.keys():
                mydict[num].append(idx)
            else:
                mydict[num] = [idx]

        for num in nums:
            # checks if target is a result of sum of same number residing in two different idx's
            if (target - num == num):
                if len(mydict.get(num)) >= 2:
                    return mydict.get(num)[:2]
                continue

            # checks if target-num is in the dictionary
            elif mydict.get(target - num):
                return [mydict.get(num)[0], mydict.get(target - num)[0]]
        return None

#leetcode 1816. Truncate Sentence
from functools import reduce
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        l=s.split()
        return reduce(lambda x,y: x+" "+y,l[:k])
    #one line also possible
    #return ' '.join(str(i) for i in list(s.split(" "))[:k])
"""
Input: s = "Hello how are you Contestant", k = 4
Output: "Hello how are you"
"""

#26. Remove Duplicates from Sorted Array
def removeDuplicates(self, nums: List[int]) -> int:
    #condition we can't use extra space in this problem need to modify the same array
    #solution1 O(nlogn) because of sorting
    nums[:] = sorted(set(nums))
    return len(nums)
    #soltuion 2 O(n) but array still contains no. of ele as many as there are previous
    #but some of them are override by other elements.
    i = 0
    for j in range(1, len(nums)):

        if nums[i] != nums[j]:
            nums[i + 1] = nums[j]
            i += 1
    return i + 1 #return then length of string


    #solution 3: very slow almost O(n^2)
    count = 0
    for i in range(len(nums)):
        # if nums[i]!=nums[i+1]: it will give the index out of range error

        if nums[i] not in nums[i + 1:]: #using this we will search entire list agings to find that if same element is present or not
            count += 1
            nums[count - 1] = nums[i]

    return count




