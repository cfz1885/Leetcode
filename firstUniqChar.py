import collections

class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = collections.Counter(s)
        for index, ch in enumerate(s):
            if cnt[ch] == 1:
                return index
        return -1