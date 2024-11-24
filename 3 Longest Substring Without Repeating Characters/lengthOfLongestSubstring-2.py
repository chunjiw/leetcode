class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        letters = set()
        long = 0
        i, j = 0, 0
        while j < n:
            if s[j] not in letters:
                letters.add(s[j])
                long = max(long, len(letters))
            else:
                while s[i] != s[j]:
                    letters.remove(s[i])
                    i += 1
                i += 1
            j += 1
        return long

sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
print(sol.lengthOfLongestSubstring("bbbbb"))
print(sol.lengthOfLongestSubstring("pwwkew"))