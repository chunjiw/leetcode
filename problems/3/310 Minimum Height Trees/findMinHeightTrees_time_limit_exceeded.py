from collections import deque
import sys

class Solution:

    def findMinHeight(self, i, neighbors, currMinHeight):
        queue = deque([i])
        visited = set([i])
        height = 0
        while queue:
            height += 1
            if height > currMinHeight:
                break
            for _ in range(len(queue)):
                for node in neighbors[queue.popleft()]:
                    if node not in visited:
                        visited.add(node)
                        queue.append(node)
        return height

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        neighbors = [[] for _ in range(n)]
        for a, b in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)
        minHeight = sys.maxsize
        result = []
        for i in range(n):
            height = self.findMinHeight(i, neighbors, minHeight)
            if height < minHeight:
                minHeight = height
                result = [i]
            elif height == minHeight:
                result.append(i)
        return result