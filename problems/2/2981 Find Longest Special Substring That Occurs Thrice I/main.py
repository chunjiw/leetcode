class Solution:
    def maximumLength(self, s: str) -> int:
        result = -1
        i, j = 0, 0
        n = len(s)
        count = dict()
        while j < n:
            while j < n and s[i] == s[j]:
                j += 1
            icount = count.get(s[i], dict())
            for k in range(1, j - i + 1):
                icount[k] = icount.get(k, 0) + j - i + 1 - k
            count[s[i]] = icount
            i = j
        for icount in count.values():
            for length, rep in icount.items():
                if rep >= 3:
                    result = max(result, length)
        return result

sol = Solution()
print(sol.maximumLength("aaaa"))
print(sol.maximumLength("abcdef"))
print(sol.maximumLength("abcaba"))
print(sol.maximumLength("aaa_aaa_aaaa_aaaa"))
