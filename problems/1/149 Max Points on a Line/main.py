from typing import List

class Solution:

    def isLine(self, p0, p1, p2) -> bool:
        x0, y0 = p0[0], p0[1]
        x1, y1 = p1[0], p1[1]
        x2, y2 = p2[0], p2[1]
        return x0*y1 + x1*y2 + x2*y0 == x2*y1 + x1*y0 + x0*y2

    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 2:
            return n
        result = 0
        for i, pi in enumerate(points):
            for j in range(i+1, n):
                pj = points[j]
                curr_len = 2
                for k in range(j+1, n):
                    pk = points[k]
                    if self.isLine(pi, pj, pk):
                        curr_len += 1
                result = max(result, curr_len)
        return result
