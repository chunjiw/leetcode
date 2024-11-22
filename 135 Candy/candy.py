from typing import List

class Solution:

    def sumcandy(self, rl, fl):
        return rl * (rl-1) // 2 + fl * (fl-1) // 2 + max(rl, fl)

    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        result = 0
        # loop over ratings
        rl, fl = 0, 0
        risingBefore = True
        for i in range(1, n):
            if ratings[i-1] == ratings[i]:
                result += self.sumcandy(rl, fl)
                risingBefore = True
                rl, fl = 0, 0
            elif ratings[i-1] < ratings[i]:
                if risingBefore:
                    rl += 1
                else:    # falling turns to rising
                    result += self.sumcandy(rl, fl)
                    risingBefore = True
                    rl, fl = 1, 0
            else:
                if not risingBefore:
                    fl += 1
                else:    # risingBefore turns to falling
                    risingBefore = False
                    fl = 1
        result += self.sumcandy(rl, fl)
        return result + n


sol = Solution()
print(sol.candy([1,3,2,2,1]))
print(sol.candy([1,3,2]))
print(sol.candy([2,1]))

