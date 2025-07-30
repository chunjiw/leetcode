from collections import deque, defaultdict

class Solution:
    def numBusesToDestination(self, routes: list[list[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        graph = defaultdict(set)
        for route in routes:
            for i in range(len(route)):
                for j in range(i+1, len(route)):
                    graph[route[i]].add(route[j])
                    graph[route[j]].add(route[i])
        print(graph)
        level = deque([source])
        visited = {source}
        hops = 0
        while level:
            hops += 1
            for _ in range(len(level)):
                for neighbor in graph[level.popleft()]:
                    if neighbor in visited:
                        continue
                    if neighbor == target:
                        return hops
                    level.append(neighbor)
                    visited.add(neighbor)
        return -1

sol = Solution()
print(sol.numBusesToDestination([[1,2,7],[3,6,7]], 1, 6))