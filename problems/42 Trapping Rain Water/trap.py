from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        m = 0
        for i in range(n):
            if m <= height[i]:
                m = height[i]
                lastmaxindex = i
        left_high = 0
        to_trap = 0
        trapped = 0
        for i in range(n):
            if i == lastmaxindex + 1:
                break
            h = height[i]
            if h < left_high:
                to_trap += left_high - h
            else:
                left_high = h
                trapped += to_trap
                to_trap = 0
        left_high = 0
        to_trap = 0
        for i in range(n-1, lastmaxindex-1, -1):
            h = height[i]
            if h < left_high:
                to_trap += left_high - h
            else:
                left_high = h
                trapped += to_trap
                to_trap = 0
        return trapped

sol = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
# height = [4,2,0,3,2,4,3,4]
print(sol.trap(height))