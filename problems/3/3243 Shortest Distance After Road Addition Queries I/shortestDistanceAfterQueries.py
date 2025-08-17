from typing import List

from collections import deque

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for i in range(1, n):
            graph[i].append(i - 1)
        distances = list(range(n-1, -1, -1))
        result = []
        for src, dest in queries:
            graph[dest].append(src)
            queue = deque([dest])
            while queue:
                current_dest = queue.popleft()
                for src in graph[current_dest]:
                    if  distances[src] > distances[current_dest] + 1:
                        distances[src] = distances[current_dest] + 1
                        queue.append(src)
            result.append(distances[0])
        return result

sol = Solution()
result = sol.shortestDistanceAfterQueries(5, [[2,4],[0,2],[0,4]])
print(result)
