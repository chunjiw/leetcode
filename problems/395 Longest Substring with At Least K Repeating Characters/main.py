from collections import Counter

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        freq = Counter(s)
        if all([v >= k for v in freq.values()]):
            return len(s)
        i = 0
        j = 0
        result = 0
        while j < len(s):
            while j < len(s) and freq[s[j]] >= k:
                j += 1
            # here, s[i:j] is potentially solution; freq[s[j]] < k
            result = max(result, self.longestSubstring(s[i:j], k))
            i = j + 1
            j = j + 1
        return result

sol = Solution()
print(sol.longestSubstring('aaabb', 3))
print(sol.longestSubstring('ababbc', 2))
print(sol.longestSubstring('cababbc', 2))
print(sol.longestSubstring('cabeabbc', 2))

