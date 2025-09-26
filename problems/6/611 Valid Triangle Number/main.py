class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        for i in range(n):
            m = i+1
            for j in range(i+2, n):
                # if nums[m] is good?
                while nums[i] + nums[m] <= nums[j] and m < j:
                    m += 1
                res += j - m
        return res
    

sol = Solution()
print(sol.triangleNumber([2,2,3,4]))
print(sol.triangleNumber([4,2,3,4]))

