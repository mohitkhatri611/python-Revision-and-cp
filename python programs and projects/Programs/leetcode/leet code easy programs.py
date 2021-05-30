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