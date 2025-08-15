# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

# Example 1:

# Input: n = 12
# Output: 3 
# Explanation: 12 = 4 + 4 + 4.
# Example 2:

# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.

import math
from collections import deque

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        depth = 0
        level = deque()
        level.append(n)
        while level:
            depth += 1
            size = len(level)
            for _ in range(size):
                m = level.popleft()
                maxSR = int(math.sqrt(m))
                for i in range(maxSR, 0, -1):
                    if m == i * i:
                        return depth
                    level.append(m - i * i)



