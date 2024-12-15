from heapq import heappop, heappush

class Solution:

    def gain(self, cl):
        m, n = cl[0], cl[1]
        return (n-m) / n / (n+1)

    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        queue = []
        for cl in classes:
            heappush(queue, (-self.gain(cl), cl))
        print(classes)
        n = len(classes)
        while extraStudents > 0:
            extraStudents -= 1
            cl = heappop(queue)
            cl[0] += 1
            cl[1] += 1
            heappush(queue, (-self.gain(cl), cl))
        return sum([cl[0] / cl[1] for cl in classes]) / n
