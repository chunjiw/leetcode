from collections import Counter, defaultdict
from heapq import heappop, heappush

class Solution:
    def maxSubstringLength(self, s: str) -> int:
        n = len(s)
        occurances = {}
        # O(n)
        for i, char in enumerate(s):
            if char not in occurances:
                occurances[char] = [i, i]
            occurances[char][1] = i
        # O(n * 26)
        result = -1
        for char, (first, last) in occurances.items():
            start, end = first, last    # [start,end] is potential solution
            for i in range(start, n):
                if occurances[s[i]][0] < start:
                    break
                end = max(end, occurances[s[i]][1])
                if i == end and end - start + 1 != n:
                    result = max(result, end - start + 1)
        return result

sol = Solution()
print(sol.maxSubstringLength("abba"))
print(sol.maxSubstringLength("abab"))
print(sol.maxSubstringLength("abacd"))
print(sol.maxSubstringLength("off"))