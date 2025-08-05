from typing import List
from collections import deque

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(edges) + 1
        neighbors = [set() for _ in range(n)]
        for a, b in edges:
            neighbors[a].add(b)
            neighbors[b].add(a)
        down = [set() for _ in range(n)]
        up = [-1] * n
        up[0] = 0
        queue = deque([0])
        visited = { 0 }
        while queue:
            node = queue.popleft()
            for a in neighbors[node]:
                if a not in visited:
                    down[node].add(a)
                    visited.add(a)
                    queue.append(a)
                    up[a] = node
        # print(down, up)
        # simulate the game; BFS for Alice
        result = - 10001 * n
        queue = deque([(0, 0)])    # (node, profit)
        while queue:
            for _ in range(len(queue)):
                alice, profit = queue.popleft()
                if alice == bob:
                    profit += amount[alice] // 2
                else:
                    profit += amount[alice]
                if not down[alice]:
                    result = max(result, profit)
                for a in down[alice]:
                    queue.append((a, profit))
            amount[bob] = 0
            bob = up[bob]
        return result

sol = Solution()
print(sol.mostProfitablePath( [[0,1],[1,2],[1,3],[3,4]], 3, [-2,4,2,-4,6] ) )
print(sol.mostProfitablePath( [[0,1]], 1, [-7280,2350] ))
print(sol.mostProfitablePath( [[0,2],[0,4],[1,3],[1,2]], 1, [3958,-9854,-8334,-9388,3410] ))
print(sol.mostProfitablePath( 
[[0,2],[1,4],[1,6],[2,3],[2,8],[3,7],[4,5],[6,7]], 1, [-1410,-9440,5536,-774,3044,7924,-2122,-1192,9166] ))