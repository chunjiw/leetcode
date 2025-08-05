from collections import deque, defaultdict, Counter

class Solution:
    def numBusesToDestination(self, routes: list[list[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        # stations -> buses
        buses = defaultdict(set)
        stations = defaultdict(set)
        for busId, route in enumerate(routes):
            for stationId in route:
                stations[stationId].add(busId)
                buses[busId].add(stationId)

        busGraph = defaultdict(set)
        nBus = len(routes)
        for i in range(nBus):
            for j in range(i+1, nBus):
                if any(sj in buses[i] for sj in buses[j]):
                    busGraph[i].add(j)
                    busGraph[j].add(i)
        
        sourceBuses = stations[source]
        targetBuses = stations[target]
        
        level = deque(sourceBuses)
        visited = set()
        hops = 0
        while level:
            hops += 1
            for _ in range(len(level)):
                busId = level.popleft()
                if busId in targetBuses:
                    return hops
                if busId in visited:
                    continue
                visited.add(busId)
                level.extend(busGraph[busId])
        return -1

sol = Solution()
print(sol.numBusesToDestination([[1,2,7],[3,6,7]], 1, 6))