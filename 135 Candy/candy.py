from typing import List

class Solution:

    def sumcandy(self, rl, fl):
        return rl * (rl-1) // 2 + fl * (fl-1) // 2 + max(rl, fl)

    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n < 2:
            return n
        result = 0
        # loop over ratings
        rl = 0
        fl = 0
        rising = True
        for i in range(1, n):
            if ratings[i-1] == ratings[i]:
                result += self.sumcandy(rl, fl)
                rising = True
                rl, fl = 0, 0
                continue
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
                    result += self.sumcandy(rl, fl)
                    rising = True
                    rl, fl = 1, 0
        result += self.sumcandy(rl, fl)
        return result + n


sol = Solution()
print(sol.candy([1,3,2,2,1]))
print(sol.candy([1,3,2]))
print(sol.candy([2,1]))

