from collections import Counter
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        temp = counter.most_common(k)
        res = []
        for item in temp:
            for c in item:
                res.append(c)
                break
        return res
        