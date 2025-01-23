from typing import List

from collections import deque

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        xmap, ymap = {}, {}    # map from coordinate to a set of points
        for i, j in stones:
            xlist = xmap.get(i, [])
            xlist.append((i,j))
            xmap[i] = xlist
            ylist = ymap.get(j, [])
            ylist.append((i,j))
            ymap[j] = ylist
        counted = set()
        group = 0
        for i, j in stones:
            if (i,j) in counted:
                continue
            group += 1
            queue = deque([(i,j)])
            counted.add((i,j))
            while queue:
                # get all connected stones
                x, y = queue.popleft()
                for xx, yy in xmap[x] + ymap[y]:
                    if (xx,yy) not in counted:
                        queue.append((xx,yy))
                        counted.add((xx,yy))
        return len(stones) - group
            
sol = Solution()
print(sol.removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]))