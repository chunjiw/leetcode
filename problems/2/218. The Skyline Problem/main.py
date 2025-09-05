from sortedcontainers import SortedList
from heapq import heappush, heappop

class Solution(object):
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        n = len(buildings)
        queue = []                                          # a queue of (y, height)
        sheight = SortedList(key=lambda b: (-b[0], b[1]))   # a list of (height, y)
        res = []
        for i, (x, y, h) in enumerate(buildings):
            # does this building contribute a new point?
            if not sheight or h > sheight[0][0]:
                if not res or x > res[-1][0]:
                    res.append([x,h])
                else:
                    res[-1][1] = max(res[-1][1], h)
            # push this building to existing buildings
            heappush(queue, (y,h))
            sheight.add((h,y))
            # process end points of existing buildings
            while queue and (i == n-1 or queue[0][0] < buildings[i+1][0]):
                _y, _h = heappop(queue)
                sheight.remove((_h,_y))
                # if this building is the only highest one
                if not sheight:
                    res.append([_y,0])
                elif sheight[0][0] < _h:
                    res.append([_y,sheight[0][0]])
                else:
                    pass
        return res

sol = Solution()
print(sol.getSkyline([ [2,9,10], [3,7,15], [5,12,12], [15,20,10], [19,24,8] ]))