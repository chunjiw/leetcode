# 295. Find Median from Data Stream
# DescriptionHintsSubmissionsDiscussSolution
# Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

# For example,
# [2,3,4], the median is 3

# [2,3], the median is (2 + 3) / 2 = 2.5

# Design a data structure that supports the following two operations:

# void addNum(int num) - Add a integer number from the data stream to the data structure.
# double findMedian() - Return the median of all elements so far.
# Example:

# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3) 
# findMedian() -> 2



from heapq import heappush, heappop

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left = []    # maxheap
        self.right = []   # minheap
        self.size = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if self.size == 0:
            heappush(self.right, num)
            self.size += 1
            return
        if num >= self.right[0]:
            heappush(self.right, num)
        else:
            heappush(self.left, -num)
        self.size += 1
        self.adjust()
        return
    
    def adjust(self):
        while len(self.left) > len(self.right):
            heappush(self.right, -heappop(self.left))
        while len(self.left) < len(self.right) - 1:
            heappush(self.left, -heappop(self.right))    

    def findMedian(self):
        """
        :rtype: float
        """
        if self.size == 0:
            return
        if self.size % 2:
            return self.right[0]
        else:
            return (-self.left[0] + self.right[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
