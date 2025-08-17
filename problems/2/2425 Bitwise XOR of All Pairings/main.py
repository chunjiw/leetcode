class Solution:

    def xor(self, nums):
        result = 0
        for n in nums:
            result ^= n
        return result

    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        result = 0
        if m % 2 == 1:
            result ^= self.xor(nums2)
        if n % 2 == 1:
            result ^= self.xor(nums1)
        return result