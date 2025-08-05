def numGoodPairs(self, nums):
    freq = Counter(nums)
    result = 0
    for f in freq.values():
        if f > 1:
            result += f * (f - 1) // 2
    return result