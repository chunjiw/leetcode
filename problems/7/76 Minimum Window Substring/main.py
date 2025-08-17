class Solution:
    def minWindow(self, s: str, t: str) -> str:
        map = dict()
        for l in t:
            map[l] = map.get(l, 0) + 1
        count = len(t)
        n = len(s)
        left, right = -1, -1
        result = ""
        min_len = n + 1

        # make sure s[left] is in t
        for k in range(n):
            if s[k] in map:
                left, right = k, k+1     # [left,right) is in the map; right-left is current length; s[left] in t
                map[s[left]] -= 1
                count -= 1
                break
        if left < 0:
            return result

        # sliding window
        while left < n:
            if count == 0:
                if right - left < min_len:
                    min_len = right - left
                    result = s[left:right]
                map[s[left]] += 1
                if map[s[left]] > 0:
                    count += 1
                left += 1
                while left < n and s[left] not in map:
                    left += 1
            else:
                while right < n and s[right] not in map:
                    right += 1
                if right < n:
                    if map[s[right]] > 0:
                        count -= 1
                    map[s[right]] -= 1
                    right += 1
                else:
                    break
        return result

sol = Solution()
print(sol.minWindow("ADOBECODEBANC", "ABC"))
print(sol.minWindow("a", "a"))
print(sol.minWindow("b", "a"))