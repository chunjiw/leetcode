class Solution:
    def numberOfPairs(self, points: list[list[int]]) -> int:
        res = 0
        points.sort(key=lambda p: (p[0],-p[1]))
        n = len(points)
        for i in range(n):
            xi, yi = points[i]
            ymin, ymax = -10**9-1, yi
            for j in range(i+1, n):
                xj, yj = points[j]
                if ymin < yj <= ymax:
                    res += 1
                    ymin = yj
        return res

sol = Solution()
print(sol.numberOfPairs([[1,1],[2,2],[3,3]]))
print(sol.numberOfPairs([[3,4],[1,6],[2,5],[1,4],[0,4]]))
