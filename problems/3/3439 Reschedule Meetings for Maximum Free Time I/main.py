from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]):
        duration = 0
        for i in range(k):
            duration += endTime[i] - startTime[i]
        n = len(startTime)
        if k == n:
            return eventTime - duration
        res = startTime[k] - duration

        # left from 0 to n-k-1
        # right from k+1 to n
        # there are k events in between
        for left in range(n-k):
            right = left + k + 1
            duration -= endTime[left] - startTime[left]
            duration += endTime[right-1] - startTime[right-1]
            start = endTime[left]
            end = startTime[right] if right < n else eventTime
            res = max(res, end - start - duration)
        return res

sol = Solution()
print(sol.maxFreeTime(5, 1, [1,3], [2,5]))
print(sol.maxFreeTime(10, 1, [0,2,9], [1,4,10]))
print(sol.maxFreeTime(5, 2, [0,1,2,3,4], [1,2,3,4,5]))