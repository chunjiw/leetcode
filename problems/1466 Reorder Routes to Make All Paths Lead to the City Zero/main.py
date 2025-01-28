class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        neighbor = [[] for _ in range(n)]
        for a, b in connections:
            neighbor[a].append((b,1))
            neighbor[b].append((a,0))
        result = 0
        queue = deque([0])
        visited = [False] * n
        visited[0] = True
        while queue:
            i = queue.popleft()
            for j, w in neighbor[i]:
                if visited[j]:
                    continue
                queue.append(j)
                visited[j] = True
                result += w
        return result