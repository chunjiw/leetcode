from typing import List

class Solution:
    
    def trap0(self, height):
        left_high = 0
        to_trap = 0
        trapped = 0
        for h in height:
            if h < left_high:
                to_trap += left_high - h
            else:
                left_high = h
                trapped += to_trap
                to_trap = 0
        return trapped

    def trap(self, height: List[int]) -> int:
        n = len(height)
        m = 0
        mi = []
        for i in range(n):
            m = max(m, height[i])
        for i in range(n):
            if height[i] == m:
                mi.append(i)
        left = self.trap0(list(height[0:mi[0]+1]))
        hs = list(height[mi[-1]:])
        hs.reverse()
        right = self.trap0(hs)
        res = left + right
        for i in range(len(mi) - 1):
            hs = list(height[mi[i]:mi[i+1]+1])
            res += self.trap0(hs)
        return res

sol = Solution()
# height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [4,2,0,3,2,4,3,4]
print(sol.trap(height))