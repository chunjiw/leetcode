from typing import List

class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        k -= 1
        l = 1
        i = 0
        while l <= k:
            l *= 2
            i += 1
        # here, length is enough to contain k after i operations
        # reduce k until k == 0
        ops = 0
        # print(k, l)
        while k > 0:
            l //= 2
            i -= 1
            if k >= l:
                k -= l
                ops += operations[i]
            # print(k, l)
        return chr(ord('a') + ops % 26)

sol = Solution()
print(sol.kthCharacter(10, [0,1,0,1]))
print(sol.kthCharacter(5, [0,0,0]))

