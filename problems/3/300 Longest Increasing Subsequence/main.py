class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        ord = []
        for num in nums:
            if not ord or ord[-1] < num:
                ord.append(num)
                continue
            # binary search for first i so that num <= ord[i]
            i, j = 0, len(ord) - 1
            while i < j:
                m = (i+j) // 2
                if num > ord[m]:
                    i = m + 1
                else:
                    j = m
            ord[i] = num
        return len(ord)                    

             