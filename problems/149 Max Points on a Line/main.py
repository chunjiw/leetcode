from typing import List

class Solution:

    def isLine(self, p0, p1, p2) -> bool:
        x0, y0 = p0[0], p0[1]
        x1, y1 = p1[0], p1[1]
        x2, y2 = p2[0], p2[1]
        return x0*y1 + x1*y2 + x2*y0 == x2*y1 + x1*y0 + x0*y2

    def getTwo(self, line):
        it = iter(line)
        return next(it), next(it)

    def maxPoints(self, points: List[List[int]]) -> int:
        lines = []
        n = len(points)
        if n < 2:
            return n
        for i, pointi in enumerate(points):
            for j, pointj in enumerate(points[i+1:]):
                already_in = False
                pi = (pointi[0], pointi[1])
                pj = (pointj[0], pointj[1])
                for line in lines:
                    p1, p2 = self.getTwo(line)
                    if self.isLine(p1, p2, pi) and self.isLine(p1, p2, pj):
                        already_in = True
                        line.add(pi)
                        line.add(pj)
                        break
                if not already_in:
                    lines.append(set([pi, pj]))
        return max([len(line) for line in lines])