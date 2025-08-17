from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 0:
            return []
        if n == 1:
            return [0]

        neighbors = [set() for _ in range(n)]
        
        for i, j in edges:
            neighbors[i].add(j)
            neighbors[j].add(i)

        leaves = [i for i in range(n) if len(neighbors[i]) == 1]

        while n > 2:
            new_leaves = []
            for leaf in leaves:
                stem = neighbors[leaf].pop()
                neighbors[stem].remove(leaf)
                if len(neighbors[stem]) == 1:
                    new_leaves.append(stem)
            n -= len(leaves)
            leaves = new_leaves
        
        return leaves


sol = Solution()
print(sol.findMinHeightTrees(4, [[1,0],[1,2],[1,3]]))
print(sol.findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]))
print(sol.findMinHeightTrees(6, [[0,1],[0,2],[0,3],[3,4],[4,5]]))