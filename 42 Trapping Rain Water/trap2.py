# O(2n), O(2n)

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftmax = list(height)
        rightmax = list(height)
        lm, rm = 0, 0
        for i in range(n):
            leftmax[i], rightmax[-i-1] = lm, rm
            lm = max(lm, height[i])
            rm = max(rm, height[-i-1])
        result = 0
        for i in range(n):
            delta = min(leftmax[i], rightmax[i]) - height[i]
            result += max(0, delta)
        return result

sol = Solution()
# height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [4,2,0,3,2,4,3,4]
print(sol.trap(height))
