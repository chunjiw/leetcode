class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if citations[-1] == 0:
            return 0
        # search for the first i such that citations[i] >= n - i
        # then the answer is n - i
        # it is guaranteed to exist
        n = len(citations)
        i, j = 0, n - 1
        while i < j:
            m = i + (j - i) // 2
            if citations[m] < n - m:
                i = m + 1
            else:
                j = m
        return n - i

# 0 1 2 3 4
# 0 1 3 5 6
# i   m   j
# i m j
#     i