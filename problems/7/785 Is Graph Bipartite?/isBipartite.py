from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        unvisited = set(range(len(graph)))
        while unvisited:
            node = unvisited.pop()
            queue = deque([node])
            sets = [set([node]), set()]
            s = 0
            while queue:
                for _ in range(len(queue)):
                    nodes = graph[queue.popleft()]
                    for node in nodes:
                        if node in sets[s]:
                            return False
                        if node not in sets[1-s]:
                            sets[1-s].add(node)
                            queue.append(node)
                            unvisited.remove(node)
                s = 1 - s
        return True
            