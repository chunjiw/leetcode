class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        def countTarget(edges, k):
            n = len(edges) + 1
            graph = [[] for _ in range(n)]
            for a, b in edges:
                graph[a].append(b)
                graph[b].append(a)
            count = [0] * n
            K = k
            for root in range(n):
                # count targets for root
                queue = deque([root])
                visited = set([root])
                k = K
                while k >= 0:
                    k -= 1
                    count[root] += len(queue)
                    if not queue or k < 0:
                        break
                    for _ in range(len(queue)):
                        a = queue.popleft()
                        for b in graph[a]:
                            if b not in visited:
                                visited.add(b)
                                queue.append(b)
            return count

        count1 = countTarget(edges1, k)
        count2 = countTarget(edges2, k-1)
        add2 = max(count2)
        return [c + add2 for c in count1]        