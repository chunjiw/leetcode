from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n-1
        lmax, rmax = 0, 0
        water = 0
        while left <= right:
            if lmax <= rmax:
                if lmax >= height[left]:
                    water += lmax - height[left]
                else:
                    lmax = height[left]
                left += 1
            else:
                if rmax >= height[right]:
                    water += rmax - height[right]
                else:
                    rmax = height[right]
                right -= 1
        return water

sol = Solution()
# height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [4,2,0,3,2,4,3,4]
print(sol.trap(height))
