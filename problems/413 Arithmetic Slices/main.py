class Solution:
    def numberOfAriSub(self, nums):
        if len(nums) < 3:
            return 0
        # calculate diff array, return number of subarrays with same elements of at least length two
        for i in range(len(nums) - 1):
            nums[i] = nums[i + 1] - nums[i]
        nums.pop()
        result = 0
        i, j = 0, 1
        while j < len(nums):
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            # here, nums[j] is a different value
            l = j - i
            result += l * (l-1) // 2
            i = j
            j += 1
        return result        