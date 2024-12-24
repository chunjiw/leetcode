from typing import List

class Solution:

    def diameter(self, edges):
        n = len(edges) + 1
        adjacency = [set() for _ in range(n)]
        for a, b in edges:
            adjacency[a].add(b)
            adjacency[b].add(a)
        diameter = 0
        n_edges = n - 1
        while n_edges > 1:
            leaves = [a for a in range(n) if len(adjacency[a]) == 1]
            for leaf in leaves:
                stem = adjacency[leaf].pop()
                adjacency[stem].remove(leaf)
                n_edges -= 1
            diameter += 2
        return diameter + n_edges

    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        d1 = self.diameter(edges1)
        d2 = self.diameter(edges2)
        d = d1//2 + d1%2 + d2//2 + d2%2 + 1
        return max(d1, d2, d)

sol = Solution()
edges1 = [[0,1],[2,0],[3,2],[3,6],[8,7],[4,8],[5,4],[3,5],[3,9]]
edges2 = [[0,1],[0,2],[0,3]]
# print(sol.diameter(edges1))
# print(sol.diameter(edges2))
print(sol.minimumDiameterAfterMerge(edges1, edges2))
