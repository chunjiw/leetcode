class Solution:
    def smallestSubarrays(self, nums: list[int]) -> list[int]:
        # from right to left, keep smallest subarray while maintain maximum OR
        n = len(nums)
        mor = 0
        lastOnesIndex = [-1] * 31
        result = [1] * n
        for i in range(n-1, -1, -1):
            for b in range(31):
                if nums[i] >> b & 1 == 1:
                    lastOnesIndex[b] = i
            mor |= nums[i]    # maximum OR of nums[i:]
            if mor != 0:
                j = max(lastOnesIndex)
                result[i] = j - i + 1
        return result
    
sol = Solution()
print(sol.smallestSubarrays([1,0,2,1,3]))
print(sol.smallestSubarrays([1,2]))
print(sol.smallestSubarrays([1,0]))