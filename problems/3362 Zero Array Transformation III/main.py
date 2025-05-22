from heapq import heappush, heappop
from typing import List

class Solution:

    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort(key = lambda x: (x[0], -x[1]))
        n = len(nums)
        nq = len(queries)

        queue = []
        k = 0
        
        diff = [0] * (n+1)
        curr = 0
        used = 0
        for i in range(n):
            curr += diff[i]
            # put intervals that cover i to queue
            while k < nq and queries[k][0] <= i <= queries[k][1]:
                heappush(queue, (-queries[k][1], queries[k][0]))
                k += 1
            # select intervals to cover i
            while curr < nums[i]:
                if not queue:
                    return -1
                nb, a = heappop(queue)
                b = -nb
                if b < i:
                    return -1
                curr += 1
                used += 1
                diff[b+1] -= 1
            # discard intervals that are unused and does not cover i+1 and beyond
            # seems no efficient way to do this / probably unnecessary
        return nq - used

sol = Solution()
print(sol.maxRemoval([2,0,2], [[0,2], [0,2], [1,1]]))
print(sol.maxRemoval([1,1,1,1], [[1,3], [0,2], [1,3], [1,2]]))
print(sol.maxRemoval([1,2,3,4], [[0,3]]))

