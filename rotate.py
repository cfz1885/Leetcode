from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.reverse()
        
        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        reverse(nums,0, k-1)
        reverse(nums,k, len(nums)-1)

if __name__=="__main__":
    solution = Solution()
    nums = [-1,-100,3,99]
    k = 2
    solution.rotate(nums, k)


