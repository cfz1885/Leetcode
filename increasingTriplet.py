from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        minVal = float('inf')
        midVal = float('inf')
        for i in nums:
            if i <= minVal:
                minVal = i
            elif i <= midVal:
                midVal =  i
            elif i > midVal:
                return True
        return False
