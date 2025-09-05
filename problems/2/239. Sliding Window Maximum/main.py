# mono queue, strictly decreasing, first one is current max 

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        queue = deque()
        res = []
        for i in range(n):
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)
            if i >= k and queue[0] == i-k:
                queue.popleft()
            if i >= k-1:
                res.append(nums[queue[0]])
        return res
    
sol = Solution()
print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))