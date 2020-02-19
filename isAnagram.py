from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False
        strList_1 = list(s)
        strList_2 = list(t)
        strList_1.sort()
        strList_2.sort()
        for i in range(len(strList_1)):
            if not strList_1[i] == strList_2[i]:
                return False
        return True
        



if __name__ == "__main__":
    solution = Solution()
    s = "😂😀"
    t = "😀😂"
    if solution.isAnagram(s, t):
        print('Yes')
    else:
        print('No')
