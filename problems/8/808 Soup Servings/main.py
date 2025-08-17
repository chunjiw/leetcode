import math
from functools import cache

class Solution:
    def soupServings(self, n: int) -> float:
        m = math.ceil(n / 25)

        if m > 250:
            return 1.0
        
        @cache
        def recursion(i, j):
            if i == 0 and j > 0:
                return 1
            if i > 0 and j == 0:
                return 0
            if i == j == 0:
                return 1/2
            return 1/4 * (recursion(max(0,i-4), j) + recursion(max(0,i-3), j-1) + recursion(max(0,i-2), max(0,j-2)) + recursion(max(0,i-1), max(0,j-3)))
        
        return recursion(m, m)
    
sol = Solution()
print(sol.soupServings(50))
print(sol.soupServings(100))