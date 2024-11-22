from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n < 2:
            return n
        # break the array if neighbors have same ratings
        for i in range(1, n):
            if ratings[i - 1] == ratings[i]:
                return self.candy(ratings[:i]) + self.candy(ratings[i:])
        result = 0
        # decreasing ratings on the left
        broken = False
        for i in range(n - 1):
            if ratings[i] < ratings[i+1]:
                result += i * (i+1) // 2
                broken = True
                break
        if not broken:
            return (n+1) * n // 2
        # decreasing ratings on the right
        broken = False
        for j in range(n - 1):
            if ratings[-j-2] > ratings[-j-1]:
                result += j * (j+1) // 2
                broken = True
                break
        if not broken:
            return (n+1) * n // 2
        # from here, from i to n-j-1 (include), is minimum to minimum.
        # there should be other m (>=0) minimums, and m + 1 maximums.
        mi = [i]
        ma = []
        for k in range(i+1, n-j-1):
            if ratings[k] < min(ratings[k-1], ratings[k+1]):
                mi.append(k)
            if ratings[k] > max(ratings[k-1], ratings[k+1]):
                ma.append(k)
        mi.append(n-j-1)
        for k in range(len(ma)):
            left = ma[k] - mi[k]
            right = mi[k+1] - ma[k]
            result += left * (left-1) // 2 + right * (right-1) // 2 + max(left, right)
        return result + n

sol = Solution()
print(sol.candy([1,3,2,2,1]))
print(sol.candy([1,3,2]))
print(sol.candy([2,1]))

