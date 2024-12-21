from typing import List

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = [set() for _ in range(n)]
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        components = 1
        n_edges = n - 1
        while n_edges > 0:
            # recursively remove all leaves
            for a in range(n):
                while len(graph[a]) == 1:
                    if values[a] % k == 0:
                        components += 1
                    b = graph[a].pop()
                    graph[b].remove(a)
                    values[b] += values[a]
                    n_edges -= 1
                    a = b
        return components

sol = Solution()
print(sol.maxKDivisibleComponents(5, [[0,2],[1,2],[1,3],[2,4]], [1,8,1,4,4], 6))
print(sol.maxKDivisibleComponents(3, [[1,2],[2,0]], [0,2,2], 4))
