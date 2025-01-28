class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        neighbor = [[] for _ in range(n)]
        order = [set() for _ in range(n)]
        for a, b in connections:
            order[a].add(b)
            neighbor[a].append(b)
            neighbor[b].append(a)
        result = 0
        queue = deque([0])
        visited = [False] * n
        visited[0] = True
        while queue:
            i = queue.popleft()
            for j in neighbor[i]:
                if visited[j]:
                    continue
                queue.append(j)
                visited[j] = True
                if i not in order[j]:
                    result += 1
        return result