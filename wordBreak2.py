from typing import List
from collections import deque

class Solution:

    def wordBreak(self, s: str, wordDict: List[str]):
        # 寻找分割点
        size = len(s)
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        print(dp)
        res = []
        if dp[-1]:
            queue = deque()
            self.dfs(s, size, wordDict, res, queue, dp)
        return res

    def dfs(self, s, length, wordDict, res, path, dp):
        # 最后一层的情况
        if length == 0:
            res.append(' '.join(path))
            return
        
        # 其他层的情况
        for i in range(length):
            if dp[i]:# 满足条件向下搜索，代表前i个可分
                suffix = s[i:length]   #从第i个到查找的最后一个
                if suffix in wordDict:
                    path.appendleft(suffix)
                    self.dfs(s, i, wordDict, res, path, dp)
                    path.popleft()

        

if __name__=="__main__":
    s = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    solution = Solution()
    result = solution.wordBreak(s, wordDict)
    print(result)


    