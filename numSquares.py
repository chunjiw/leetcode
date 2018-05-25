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

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        self.result = n
        self.dfs(n, 0)
        return self.result

    def dfs(self, n, nSummates):
        if nSummates > self.result:
            return
        if n == 0:
            self.result = min(nSummates, self.result)
            return
        maxSR = int(math.sqrt(n))
        for i in range(maxSR, 0, -1):
            self.dfs(n - i * i, nSummates + 1)





