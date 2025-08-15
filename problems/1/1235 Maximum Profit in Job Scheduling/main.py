from functools import cache

class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        n = len(startTime)
        
        intervals = [[startTime[i], endTime[i], profit[i]] for i in range(n)]
        intervals.sort()

        @cache
        def recursion(i):
            """
            get max profit achievable start from job i
            """
            if i == n:
                return 0
            p = intervals[i][2]
            k = next(i)
            if k == n:
                return p
            else:
                # print(i, max(p + recursion(j) for j in range(k, n)))
                return max(p + recursion(j) for j in range(k, n))

        def next(k):
            """
            get next interval that does not conflict with current one
            """
            # binary search for first i such that intervals[i][0] >= intervals[k][1]
            i, j = k+1, n
            while i < j:
                m = (i+j) // 2
                if intervals[m][0] < intervals[k][1]:
                    i = m + 1
                else:
                    j = m
            return i

            # for k in range(i+1, n):
            #     if intervals[i][1] <= intervals[k][0]:
            #         return k
            # return -1

        def prev(i):
            """
            get previous interval that does not conflict with current one
            """
            for k in range(i-1, -1, -1):
                if intervals[k][1] <= intervals[i][0]:
                    return k
            return -1
        
        return recursion(0)
        
sol = Solution()

print(sol.jobScheduling([1,2,3,3], [3,4,5,6], [50,10,40,70]))
# [1,3,50], [2,4,10], [3,5,40], [3,6,70]
# r(3) = 70
# r(2) = 40
# r(1) = 10
# r(0) = 50 + 70 = 120



print(sol.jobScheduling([0,2,2,7], [1,3,7,10], [3,5,8,1]))
# [0,1,3] [2,3,5] [2,7,8], [7,10,1]
# recursion(3) = 1
# recursion(2) = 8 + r(3) = 9
# r(1) = 5 + 1 = 6
# r(0) = 3 + max(r(1), r(2), r(3)) = 3 + 9 = 12

print(sol.jobScheduling([0,2,2,7], [1,3,7,10], [3,8,5,1]))
# [0,1,3] [2,3,8] [2,7,5], [7,10,1]
# recursion(3) = 1
# recursion(2) = 5 + r(3) = 6
# r(1) = 8 + 1 = 9
# r(0) = 3 + max(r(1), r(2), r(3)) = 3 + 9 = 12
