class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        result = 1
        for i in range(n):
            prod = d = m = nums[i]
            for j in range(i+1, n):
                prod *= nums[j]
                d = math.gcd(nums[j], d)
                m = math.lcm(nums[j], m)
                if prod == d * m and result < j - i + 1:
                    result = j - i + 1
        return result
