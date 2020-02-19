from typing import  List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        tire = {} # 构建字典树
        for word in words:
            currentNode = tire
            for c in word:
                currentNode = currentNode.setdefault(c, {})
            currentNode['end'] = True
        # 字典树构建完成

        res = set() # 结果列表
        h = len(board)
        w = len(board[0])

        def dfs(i, j, node, pre, visited):
            if 'end' in node:
                res.add(pre)
            for(di, dj) in ((-1, 0), (1, 0), (0, -1), (0, 1)): #四联通
                _i, _j = i + di, j + dj
                if -1 < _i < h and -1 < _j < w and board[_i][_j] in node and (_i, _j) not in visited: # 继续搜索条件
                    dfs(_i, _j, node[board[_i][_j]], pre+board[_i][_j], visited | {(_i, _j)})
        
        for i in range(h):
            for j in range(w):
                if board[i][j] in tire:
                    dfs(i, j, tire[board[i][j]], board[i][j], {(i, j)})
        return res

