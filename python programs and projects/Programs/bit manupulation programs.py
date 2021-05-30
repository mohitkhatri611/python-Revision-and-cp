# leetcode 136. Single Number
class Solution:
    def singleNumber(self, nums):

        #using list manupulation of x-or
        res=0
        for i in nums:
            res ^= i
        return res

"""
        #way 2 using brute force
        dct = {}

        for i in nums:
            if i in dct:
                dct[i] = 2
            else:
                dct[i] = i

        print(dct)
        for k in dct.values():
            if k != 2:
                # print(k)
                return k
"""