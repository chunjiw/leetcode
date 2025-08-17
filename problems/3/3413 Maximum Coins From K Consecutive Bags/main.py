from typing import List

class Solution:
        
    def index(self, coins, x):
        # binary search for index of bag that contains number x
        i, j = 0, len(coins) - 1
        while i < j:
            m = i + (j - i) // 2
            l, r, _ = coins[m]
            if l <= x <= r:
                return (True, m)
            elif r < x:
                i = m + 1
            else:
                j = m
        l, r, _ = coins[i]
        if l <= x <= r:
            return (True, i)    
        # if not found, return index of last interval that is smaller than x
        if x < coins[i][0]:
            return (False, i-1)
        return (False, i)

    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        curr = result = 0
        coins.sort()
        n = len(coins)
        prefixsum = [0] * (n + 1)
        prefixsum[0] = coins[0][2] * (coins[0][1] - coins[0][0] + 1)
        for i in range(1, n):
            prefixsum[i] = prefixsum[i-1] + coins[i][2] * (coins[i][1] - coins[i][0] + 1)

        for i, (start, end, _) in enumerate(coins):
            y = start + k - 1
            found, j = self.index(coins, y)
            if not found:
                curr = prefixsum[j] - prefixsum[i-1]
            else:
                curr = prefixsum[j-1] - prefixsum[i-1]
                l, _, c = coins[j]
                curr += c * (y - l + 1)
            result = max(result, curr)
            
            x = end - k + 1
            found, j = self.index(coins, x)
            if not found:
                curr = prefixsum[i] - prefixsum[j]
            else:
                curr = prefixsum[i] - prefixsum[j]
                _, r, c = coins[j]
                curr += c * (r - x + 1)
            result = max(result, curr)
        return result

sol = Solution()
print(sol.maximumCoins([[8,10,1],[1,3,2],[5,6,4]], 4))
# sol.index([[1,3,2],[5,6,4],[8,10,1]], 8)