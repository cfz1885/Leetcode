from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        length = len(s)
        mid = int(length/2)
        for i in range(mid):
            s[-i-1], s[i] = s[i], s[-i-1]
        
        """
        其实，s.reverse()就可以...
        """
        

if __name__ == "__main__":
    solution = Solution()
    strmy = "hello"
    listStr = list(strmy)
    solution.reverseString(listStr)