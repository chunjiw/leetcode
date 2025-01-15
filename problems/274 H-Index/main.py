class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        # (eventually) delta[i] is number of papers that has at least i+1 citations
        delta = [0] * (n + 1)    # delta[-1] = 0   
        for c in citations:
            if c == 0:
                continue
            delta[0] += 1
            if c <= n-1:
                delta[c] -= 1
        result = 0
        for i in range(n):
            delta[i] += delta[i-1]
            if delta[i] >= i+1:
                result = i+1
        return result
            
