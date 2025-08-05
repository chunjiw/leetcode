class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        top_freq = max(freq.values())
        top_freq_count = sum(value == top_freq for value in freq.values())
        intervals = (n+1) * (top_freq-1) + top_freq_count
        left = len(tasks) - intervals
        return intervals if left <= 0 else intervals + left