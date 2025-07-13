from functools import cache
from typing import List

class Solution:

    def nextStates(self, state):
        x, m, y = state
        fx, fm, fy = x, m, y
        if x == y:
            return set()
        # k = n // 2
        # first top player competes with one in y
        fy -= 1
        # k -= 1 
        if x + 1 + m < y:
            # second top player also competes with one in y
            fy -= 1
            # k -= 1
        elif x + 1 + m > y:
            # second top player competes with one in m
            fm -= 1
            # k -= 1
        # print("free state: ", fx, fm, fy)
        return self.nextFree((fx,fm,fy))

    @cache
    def nextFree(self, state):
        result = set()
        x, m, y = state
        self.nextRound(x, m, y, 0, 0, 0, result)
        return result

    def nextRound(self, x, m, y, px, pm, py, result):
        if x + m + y < 2:
            xx, mm, yy = x+px, m+pm, y+py
            if xx > yy:
                xx, yy = yy, xx
            result.add((xx, mm, yy))
            return
        if x > 0 and y > 0:
            self.nextRound(x-1, m, y-1, px+1, pm, py, result)
            self.nextRound(x-1, m, y-1, px, pm, py+1, result)
        elif m > 0 and y > 0:
            self.nextRound(x, m-1, y-1, px, pm+1, py, result)
            self.nextRound(x, m-1, y-1, px, pm, py+1, result)
        elif y > 0:
            self.nextRound(x, m, y-2, px, pm, py+1, result)
        elif m > 0:
            self.nextRound(x, m-2, y, px, pm+1, py, result)

    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        x = firstPlayer - 1
        y = n - secondPlayer
        m = n - x - y - 2
        if x > y:
            x, y = y, x
        level = { (x,m,y) }
        rnd = 1
        first, last = 10, 1
        while level:
            # print(level)
            newlevel = set()
            for state in level:
                ns = self.nextStates(state)
                if not ns:
                    first = min(first, rnd)
                    last = max(last, rnd)
                newlevel.update(ns)
            level = newlevel
            rnd += 1
        return [first, last]

sol = Solution()

# print(sol.earliestAndLatest(11, 2, 4))
# print(sol.nextFree((1,1,7)))
# print(sol.nextStates((0,0,4)))
# print(sol.nextStates((0,1,3)))

# print(sol.earliestAndLatest(5, 1, 5))

# print(sol.earliestAndLatest(3, 2, 3))

print(sol.earliestAndLatest(10, 1, 8))