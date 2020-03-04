from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        a = 0
        b = 0
        for item in tokens:
            if item not in '+-*/':
                s.append(int(item))
            elif len(s) >= 2:
                b = s.pop()
                a = s.pop()
                if item == '+':
                    s.append(a+b)
                elif item == '*':
                    s.append(a*b)
                elif item == '/':
                    s.append(int(a/b))
                elif item == '-':
                    s.append(a-b)
        res = s.pop()
        return res

if __name__=="__main__":
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    solution = Solution()
    res = solution.evalRPN(tokens)
    print(res)