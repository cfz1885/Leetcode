from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        res = []
        for i in range(len(nums2)):
            if nums2[i] in nums1:
                target = nums2[i]
                res.append(nums2[i])
                nums1.remove(target)
        return res

if __name__ == "__main__":
    solution = Solution()
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    print(solution.intersect(nums1, nums2))