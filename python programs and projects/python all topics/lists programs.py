
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

