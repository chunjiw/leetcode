from typing import List

class Solution:

    def dfs(self, i, path):
        if self.cyclefound:
            return
        for j in self.neighbor[i]:
            if path and j == path[-1]:
                continue
            if path and j in path:
                # here, cycle detected
                # the cycle is in path: [... j ...] i : from j to i
                self.cyclefound = True
                self.cycle = [j, path.copy(), i]
                return
            path.append(i)
            self.dfs(j, path)
            path.pop()

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        self.neighbor = [[] for _ in range(n + 1)]
        for a, b in edges:
            self.neighbor[a].append(b)
            self.neighbor[b].append(a)
        self.cyclefound = False
        self.dfs(1, [])
        j, path, i = self.cycle
        cycle = path[path.index(j):]
        cycle.append(i)
        cycleEdges = set()
        for k in range(len(cycle)-1):
            cycleEdges.add((cycle[k], cycle[k+1]))
        for a, b in reversed(edges):
            if (a, b) in cycleEdges or (b, a) in cycleEdges:
                return [a, b]

sol = Solution()
print(sol.findRedundantConnection([[1,2],[1,3],[2,3]]))