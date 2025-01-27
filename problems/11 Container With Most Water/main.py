# 2:56 pm

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        if n < 2:
            return 0
        i, j = 0, n - 1
        result = 0
        while i < j:
            result = max(result, min(height[i], height[j]) * (j - i))
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return result
        