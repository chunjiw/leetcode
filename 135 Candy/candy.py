from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings:
            return 0
        prev = ratings[0]
        up, down, peak, res = 0, 0, 0, 0
        for curr in ratings[1:]:
            if prev == curr:
                up, down, peak = 0, 0, 0
            elif prev < curr:
                up += 1
                peak = up
                res += up
                down = 0
            else:
                down += 1
                res += down
                if down <= peak:
                    res -= 1
                up = 0
            prev = curr
        return res + len(ratings)

sol = Solution()
print(sol.candy([1,3,2,2,1]))
print(sol.candy([1,3,2]))
print(sol.candy([2,1]))

