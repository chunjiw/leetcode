from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        curr, result = 1, 0
        flowerbed.append(0)
        flowerbed.append(1)
        m = len(flowerbed)
        for i in range(m):
            if flowerbed[i] == 0:
                curr += 1
            else:
                result += (curr - 1) // 2
                curr = 0
        return result >= n

sol = Solution()
print(sol.canPlaceFlowers([1,0,0,0,1], 1))
print(sol.canPlaceFlowers([1,0,0,0,1,0,0], 2))