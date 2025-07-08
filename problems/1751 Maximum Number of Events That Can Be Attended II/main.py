from typing import List

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        n = len(events)

        def next_event(p):
            # if p == len(events) - 1, binary search is skipped because i == j == len(events) and returned
            a, b, _ = events[p]
            # binary search for first q so that b < events[q][0]
            i, j = p+1, len(events)
            while i < j:
                m = (i + j) // 2
                if b < events[m][0]:
                    j = m
                else:
                    i = m + 1
            return i

        @cache
        def recursion(i, count):
            if count == 0:
                return 0
            if i == n:
                return 0
            a, b, v = events[i]
            j = next_event(i)
            return max(recursion(i+1, count), v + recursion(j, count-1))
        
        return recursion(0, k)

sol = Solution()
print(sol.maxValue([[1,2,4],[3,4,3],[2,3,1]], 2))
print(sol.maxValue([[1,2,4],[3,4,3],[2,3,10]], 2))
print(sol.maxValue([[1,1,1],[2,2,2],[3,3,3],[4,4,4]], 3))
