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
        # loop over ratings
        rl = 0
        fl = 0
        rising = True
        for i in range(1, n):
            if rising:
                if ratings[i-1] < ratings[i]:
                    rl += 1
                else:
                    rising = False
                    fl = 1
            else:
                if ratings[i-1] > ratings[i]:
                    fl += 1
                else:
                    rising = True
                    result += rl * (rl-1) // 2 + fl * (fl-1) // 2 + max(rl, fl)
                    rl = 1
                    fl = 0
        result += rl * (rl-1) // 2 + fl * (fl-1) // 2 + max(rl, fl)
        return result + n


sol = Solution()
print(sol.candy([1,3,2,2,1]))
print(sol.candy([1,3,2]))
print(sol.candy([2,1]))

