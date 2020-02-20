from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = 0
        for i in nums:
            if i == 0:
                cnt += 1
        if cnt > 0:
            for i in range(cnt):
                nums.remove(0)
            for i in range(cnt):
                nums.append(0)
            
