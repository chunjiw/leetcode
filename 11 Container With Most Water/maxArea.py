class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        m = 0
        while i < j:
            a = (j - i) * min(height[i], height[j])
            m = max(m, a)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return m
