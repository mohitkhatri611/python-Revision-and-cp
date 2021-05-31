#26. Remove Duplicates from Sorted Array
from typing import List


def removeDuplicates(self, nums: List[int]) -> int:
    #solution 3: very slow almost O(n^2)
    count = 0
    for i in range(len(nums)):
        # if nums[i]!=nums[i+1]: it will give the index out of range error
        #observe the below list code
        if nums[i] not in nums[i + 1:]: #using this we will search entire list agings to find that if same element is present or not
            count += 1
            nums[count - 1] = nums[i]

    #solution 2 for the
    if not nums:
        return 0
    length = 1
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[j], nums[i] = nums[i], nums[j] #observe the swapping of elements
            length += 1
    return length