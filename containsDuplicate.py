from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mySet = set(nums)
        if len(mySet) == len(nums):
            return False
        return True

if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,3,1]
    print(solution.containsDuplicate(nums))