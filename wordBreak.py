from typing import List
class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[0] = True
        i = 1
        j = 0
        for i in range(len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]

if __name__=="__main__":
    solution = Solution()
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    if solution.wordBreak(s, wordDict) :
        print('True')
    else:
        print('False')