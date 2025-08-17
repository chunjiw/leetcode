from typing import List

class Solution:

    def combineRest(self, m, n, k, base, result):
        '''
        Get combinations of k numbers chosen from m to n 
        '''
        if k == 0:
            result.append(base)
            return
        else:
            for x in range(m, n+1):
                xb = list(base)
                xb.append(x)
                self.combineRest(x + 1, n, k - 1, xb, result)

    def combine(self, n: int, k: int) -> List[List[int]]:
        base, result = [], []
        self.combineRest(1, n, k, base, result)
        return result

sol = Solution()
print(sol.combine(4, 2))