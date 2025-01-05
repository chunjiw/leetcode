from typing import List

class Solution:

    def gcd(self, m, n):
        if m > n:
            m, n = n, m
        while m > 0:
            n, m = m, n % m
        return n
        
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            gcd = nums[i]
            for j in range(i, n):
                gcd = self.gcd(gcd, nums[j])
                count += 1 if gcd == k else 0
        return count

sol = Solution()
# print(sol.subarrayGCD([9,3,1,2,6,3], 3))
print(sol.subarrayGCD([3, 12, 9, 6], 3))