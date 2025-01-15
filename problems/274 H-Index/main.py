class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        # count[i] is number of papers that has i citations
        # count[n+1] = 0
        count = [0] * (n + 2)
        for c in citations:
            count[min(c, n)] += 1
        for i in range(n, -1, -1):
            count[i] += count[i+1]
            # here count[i] is number of papers that has at least i citations
            if count[i] >= i:
                return i
            
