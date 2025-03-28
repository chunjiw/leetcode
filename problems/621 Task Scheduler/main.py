class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        bag = set(tasks)
        result = 0
        # first, schedule tasks without gap; frequent tasks take priority
        heap = [(-f, label) for label, f in freq.items()]
        heapify(heap)
        while len(heap) > n + 1:
            result += n + 1
            scheduled = []
            for _ in range(n + 1):
                neg_count, label = heappop(heap)
                if neg_count + 1 < 0:
                    scheduled.append((neg_count+1, label))
            while scheduled:
                heappush(heap, scheduled.pop())
        # here, len(heap) <= n + 1
        # Each cycle of n+1 length is enough for one task each
        if heap:
            top_freq = -heap[0][0]
            top_task_count = 0
            while heap and -heap[0][0] == top_freq:
                heappop(heap)
                top_task_count += 1
        return result + (top_freq - 1) * (n+1) + top_task_count