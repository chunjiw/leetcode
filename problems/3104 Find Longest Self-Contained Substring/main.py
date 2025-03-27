from collections import Counter

class Solution:
    def maxSubstringLength(self, s: str) -> int:
        freq = Counter(s)
        result = -1

        def contains(bag, freq):
            for key in bag:
                if bag[key] != freq[key]:
                    return False
            return True

        for i in range(len(s)):
            # substring starts from s[i]
            bag = Counter()
            for j in range(i, len(s)):
                if j-i+1 <= result:
                    continue
                bag[s[j]] += 1
                if contains(bag, freq) and (i > 0 or j < len(s)-1):
                    result = max(result, j-i+1)
        return result

sol = Solution()
print(sol.maxSubstringLength("abba"))
print(sol.maxSubstringLength("abab"))
print(sol.maxSubstringLength("abacd"))