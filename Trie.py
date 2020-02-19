class Trie:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {} # 节点有一个字典存储子节点
        self.end = -1 # 记录是否到达叶子节点
        
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        currentNode = self.root # 每一个单词开始都需要从根结点出发
        for c in word:
            if not c in currentNode: # 如果有一个不存在的字符
                currentNode[c] = {} # 创建一个新的节点，使用字典保存节点信息
            currentNode = currentNode[c] # 将当前节点移动到新的节点上
        currentNode[self.end] = True # 单词录入完成后最后一个节点是叶子节点
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        currentNode = self.root
        for c in word:
            if not c in currentNode:
                return False
            currentNode = currentNode[c]
        
        if not self.end in currentNode:
            return False

        return True 

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        currentNode = self.root
        for c in prefix:
            if not c in currentNode:
                return False
            currentNode = currentNode[c]
        
        return True 
