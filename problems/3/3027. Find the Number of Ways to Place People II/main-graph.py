class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # O(n^2)
        # from right to left, form graph.
        # for new point, check existing point, and eliminate decendants
        points.sort(key=lambda p: (p[0], -p[1]))
        n = len(points)
        res = 0
        graph = [[] for _ in range(n)]
        for i in range(n-2, -1, -1):
            xi, yi = points[i]
            invalid = set()
            for j in range(i+1, n):
                if j in invalid:
                    continue
                xj, yj = points[j]
                if xi <= xj and yi >= yj:
                    graph[i].append(j)
                    res += 1
                    # all decendents of j is invalid
                    stack = [j]
                    while stack:
                        k = stack.pop()
                        if k not in invalid:
                            invalid.add(k)
                            stack.extend(graph[k])
        return res