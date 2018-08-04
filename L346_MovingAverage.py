# 346. Moving Average from Data Stream
# DescriptionHintsSubmissionsDiscussSolution
# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

# For example,
# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1
# m.next(10) = (1 + 10) / 2
# m.next(3) = (1 + 10 + 3) / 3
# m.next(5) = (10 + 3 + 5) / 3



from collections import deque

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.stream = deque()
        self.size = size
        self.len = 0
        self.sum = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.stream.append(val)
        self.len += 1
        self.sum += val
        if self.len > self.size:
            self.len -= 1
            self.sum -= self.stream.popleft()
        return self.sum / float(self.len)
    


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
