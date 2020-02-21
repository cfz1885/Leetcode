from typing import List

class MinStack:
    
    def __init__(self): # pylint: disable=E0202
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.minStack) == 0 or x <= self.minStack[-1]:
            self.minStack.append(x) # 如果有比当前更小的值，则更新最小值
        else:
            self.minStack.append(self.minStack[-1]) # 如果没有更小的值，则继续压入一个当前最小值

    def pop(self) -> None:
        if self.stack:
            self.minStack.pop()
            return self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]