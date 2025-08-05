class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        if len(nums2) == 1:
            return nums1[0] * nums2[0]

        # guaranteed len(nums2) > 1
        
        def leftCount(num):
            """
            count of products that is less than or equal to num
            """
            res = 0
            for a in nums1:
                if a == 0:
                    if num >= 0:
                        res += len(nums2)
                elif a > 0:
                    if a * nums2[-1] <= num:
                        res += len(nums2)
                        continue
                    # binary search for first index l such that a * nums2[l] > num
                    i, j = 0, len(nums2) - 1
                    while i < j:
                        m = (i + j) // 2
                        if a * nums2[m] <= num:
                            i = m+1
                        else:
                            j = m
                    res += i
                else:    # a < 0
                    if a * nums2[0] <= num:
                        res += len(nums2)
                        continue
                    # binary search for last index l such that a * nums[l] > num
                    i, j = 0, len(nums2) - 1
                    while i < j:
                        m = (i + j + 1) // 2
                        if a * nums2[m] <= num:
                            j = m - 1
                        else:
                            i = m
                    res += len(nums2)-i-1
            return res


        i = -10**10
        j = 10**10
        # binary search for first int res such that leftCount(res) >= k
        while i < j:
            m = (i+j) // 2
            if leftCount(m) < k:
                i = m + 1
            else:
                j = m
        return i
