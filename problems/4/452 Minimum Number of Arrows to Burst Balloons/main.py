class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[0])
        point = points[0]
        count = 1
        for start, end in points[1:]:
            if point[1] < start:
                count += 1
                point[0], point[1] = start, end
            else:
                point[0] = max(point[0], start)
                point[1] = min(point[1], end)
        return count
