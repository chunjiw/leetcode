from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        result = 0
        i = 0
        while i < len(arr):
            n = arr[i]
            while i < len(arr) and i != n:
                i += 1
                n = max(n, arr[i])
            result += 1
            i = i + 1
        return result

sol = Solution()
print(sol.maxChunksToSorted([0,1,2,3,4]))
print(sol.maxChunksToSorted([1,0,2,3,4]))
print(sol.maxChunksToSorted([4,3,2,1,0]))