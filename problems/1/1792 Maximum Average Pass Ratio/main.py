class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        queue = [ ((m-n)/n/(n+1), m, n) for m, n in classes ]
        heapify(queue)
        for _ in range(extraStudents):
            _, m, n = heappop(queue)
            heappush(queue, ((m-n)/(n+1)/(n+2), m+1, n+1))
        return sum([m / n for _, m, n in queue]) / len(classes)
