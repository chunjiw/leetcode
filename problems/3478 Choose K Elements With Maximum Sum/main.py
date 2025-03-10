from typing import List

from heapq import heappush, heappop

class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        n = len(nums1)
        nums1_index = [(nums1[i], i) for i in range(n)]
        nums1_index.sort()
        nums2_aligned = [nums2[nums1_index[i][1]] for i in range(n)]
        max_sum = []
        heap = []
        curr_sum = 0
        for i in range(n):
            heappush(heap, nums2_aligned[i])
            curr_sum += nums2_aligned[i]
            if i >= k:
                curr_sum -= heappop(heap)
            max_sum.append(curr_sum)
        result = [0] * n
        for k, num in enumerate(nums1):
            # binary search for last number that is smaller than num in nums1_index
            i, j = 0, n - 1
            while i < j:
                m = i + (j - i) // 2
                if nums1_index[m][0] < num:
                    i = m + 1
                else:
                    j = m
            # here, i is the index of first num; so i - 1 is the last number that is smaller than num
            if i > 0:
                result[k] = max_sum[i-1]
        return result

sol = Solution()
print(sol.findMaxSum([4,2,1,5,3], [10,20,30,40,50], 2))
