from collections import deque

class Solution:

    def evaluate(self, graph, a, b):
        if a not in graph or b not in graph:
            return -1
        if a == b:
            return 1
        queue = deque([(a, 1)])
        seen = set([a])
        while queue:
            for _ in range(len(queue)):
                a, value = queue.popleft()
                for c, vc in graph[a]:
                    if c == b:
                        return value * vc
                    if c not in seen:
                        queue.append((c, value * vc))
                        seen.add(c)
        return -1

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = dict()
        for i, value in enumerate(values):
            a, b = equations[i]
            a_set = graph.get(a, set())
            a_set.add((b, value))
            b_set = graph.get(b, set())
            b_set.add((a, 1 / value))
            graph[a] = a_set
            graph[b] = b_set
        return [self.evaluate(graph, a, b) for a, b in queries]
