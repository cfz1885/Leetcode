from heapq import *
from typing import List
class MedianFinder:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxHeap = []
        self.minHeap = []
        heapify(self.maxHeap)
        heapify(self.minHeap)
        

    def addNum(self, num: int) -> None:
        heappush(self.minHeap, num)
        heappush(self.maxHeap, -heappop(self.minHeap)) # max堆是通过取相反数将最小堆转化为最大堆 使用时要将pop的数据取反
        if len(self.maxHeap) > len(self.minHeap):
            heappush(self.minHeap, -heappop(self.maxHeap))


    def findMedian(self) -> float:
        maxlen = len(self.maxHeap)
        minlen = len(self.minHeap)
        if maxlen == minlen:
            return (-self.maxHeap[0]+self.minHeap[0])/2
        else:
            return self.minHeap[0]/1
