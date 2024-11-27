from typing import List

from collections import deque

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        source = [[]]
        for i in range(1, n):
            source.append([i - 1])
        plen = list(range(n))
        plen.reverse()
        res = []
        for query in queries:
            source[query[1]].append(query[0])
            level = deque([query[1]])
            while level:
                for _ in range(len(level)):
                    des = level.popleft()
                    for src in source[des]:
                        if  plen[src] > plen[des] + 1:
                            plen[src] = plen[des] + 1
                            level.append(src)
            res.append(plen[0])
        return res

sol = Solution()
res = sol.shortestDistanceAfterQueries(5, [[2,4],[0,2],[0,4]])
print(res)
