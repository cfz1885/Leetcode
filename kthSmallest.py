from typing import List
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n, m = len(matrix), len(matrix[0])
        l, h = matrix[0][0], matrix[-1][-1]
        
        while l < h:
            count = 0
            mid = l + (h-l)//2
            for i in range(n):
                j = m-1
                while j>=0 and matrix[i][j]>mid:
                    j -= 1               
                count += j+1
                #print(count, k)
            if count>=k:
                h = mid
            else:
                l = mid + 1
        return l