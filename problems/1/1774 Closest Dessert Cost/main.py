# O(m * n) For each topping, can choose 0, 1, 2. So total 3^n choices

import sys

class Solution:

    def allTopCost(self, toppingCosts, i, cost, target):
        if i == len(toppingCosts):
            if abs(cost - target) < self.gap or (abs(cost - target) == self.gap and cost < target):
                self.result = cost
                self.gap = abs(cost - target)
            return
        if cost - target >= self.gap:
            return
        for k in range(3):
            self.allTopCost(toppingCosts, i+1, cost + toppingCosts[i] * k, target)

    def closestCost(self, baseCosts, toppingCosts, target):
        n = len(baseCosts)
        m = len(toppingCosts)
        self.gap = sys.maxsize
        for b in baseCosts:
            self.allTopCost(toppingCosts, 0, b, target)
        return self.result

sol = Solution()
print(sol.closestCost([1,7], [3,4], 10))     # 10
print(sol.closestCost([2,3], [4,5,100], 18)) # 17
print(sol.closestCost([3,10], [2,5], 9))     # 8
