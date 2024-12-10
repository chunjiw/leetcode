from typing import List

class Solution:

    def isLine(self, points: List[List[int]]) -> bool:
        (x0, y0) = (points[0][0], points[0][1])
        (x1, y1) = (points[1][0], points[1][1])
        (x2, y2) = (points[2][0], points[2][1])
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
                    point1, point2 = self.getTwo(line)
                    if self.isLine([point1, point2, pointi]) and self.isLine([point1, point2, pointj]):
                        already_in = True
                        line.add(pi)
                        line.add(pj)
                        break
                if not already_in:
                    lines.append(set([pi, pj]))
        return max([len(line) for line in lines])