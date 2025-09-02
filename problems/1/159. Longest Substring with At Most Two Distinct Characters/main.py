from collections import Counter

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        i = 0    # to be excluded
        freq = Counter()
        res = 0
        for j in range(0, n):
            freq[s[j]] += 1
            while len(freq) > 2:
                freq[s[i]] -= 1
                if freq[s[i]] == 0:
                    freq.pop(s[i])
                i += 1
            res = max(res, j-i+1)
        return res

sol = Solution()
print(sol.lengthOfLongestSubstringTwoDistinct('aecea'))
print(sol.lengthOfLongestSubstringTwoDistinct('aabbccc'))