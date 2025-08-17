class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        prev = 0
        result = 0
        for value in values:
            result = max(result, prev + value - 1)
            prev = max(prev - 1, value)
        return result