from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m = abs(matrix[0][0])
        res = 0
        neg_singular = 0
        for row in matrix:
            for num in row:
                res += abs(num)
                if num < 0:
                    neg_singular = 1 - neg_singular
                m = min(m, abs(num))
        return res - neg_singular * 2 * m

sol = Solution()
print(sol.maxMatrixSum([[1,2,3],[-1,-2,-3],[1,2,3]]))