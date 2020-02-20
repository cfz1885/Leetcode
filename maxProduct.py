from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return nums[0]
        maxNum = float('-inf')
        imax, imin = 1, 1
        for i in range(length):
            if nums[i] < 0:
                imax, imin = imin, imax
            imax = max(imax * nums[i], nums[i])# 针对nums[i]是0的情况
            imin = min(imin * nums[i], nums[i])
            maxNum = max(maxNum, imax)
        return maxNum

if __name__ == "__main__":
    solution = Solution()
    nums = [-4,-3]
    print(solution.maxProduct(nums))
