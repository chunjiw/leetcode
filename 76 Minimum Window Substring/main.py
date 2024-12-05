class Solution:

    def __init__(self):
        self.map = dict()

    def full(self):
        return all([curr >= total for curr, total in self.map.values()])

    def minWindow(self, s: str, t: str) -> str:
        for l in t:
            _, count = self.map.get(l, [0,0])
            self.map[l] = [0, count + 1]
        n = len(s)
        min_len = n + 1
        result = ""
        i = -1
        for k in range(n):
            if s[k] in self.map:
                i, j = k, k+1     # [i,j) is in the map; j-i is current length; s[i] in t
                self.map[s[k]][0] = 1
                break
        if i < 0:
            return result
        while i < n:
            if self.full():
                if j - i < min_len:
                    min_len = j - i
                    result = s[i:j]
                self.map[s[i]][0] -= 1
                i += 1
                while i < n and s[i] not in self.map:
                    i += 1
            else:
                while j < n and s[j] not in self.map:
                    j += 1
                if j < n:
                    self.map[s[j]][0] += 1
                    j += 1
                else:
                    break
        return result

sol = Solution()
print(sol.minWindow("ADOBECODEBANC", "ABC"))
sol = Solution()
print(sol.minWindow("a", "a"))
sol = Solution()
print(sol.minWindow("b", "a"))