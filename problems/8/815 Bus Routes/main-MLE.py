from collections import deque, defaultdict, Counter

class Solution:
    def numBusesToDestination(self, routes: list[list[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        # stations -> buses
        bus = defaultdict(set)
        for busId, route in enumerate(routes):
            for station in route:
                bus[station].add(busId)
        
        # for key, value in bus:
        #     if key != source and key != target and len(value) == 1:

        graph = defaultdict(set)
        for route in routes:
            for i in range(len(route)):
                if route[i] != source and route[i] != target and len(bus[route[i]]) == 1:
                    continue
                for j in range(i+1, len(route)):
                    if route[j] != source and route[j] != target and len(bus[route[j]]) == 1:
                        continue
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