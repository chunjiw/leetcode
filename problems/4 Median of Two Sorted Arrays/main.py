from typing import List

class Solution:

    def findMedian(self, nums):
        if not nums:
            return None
        n = len(nums)
        return nums[n//2] if n % 2 == 1 else (nums[n//2-1] + nums[n//2]) / 2

    def findMedianWithExtra(self, num, nums):
        n = len(nums)
        if n == 0:
            return num
        if n == 1:
            return (num + nums[0]) / 2
        m = n // 2
        center = nums[m-1 : m+2] if n % 2 == 1 else nums[m-1 : m+1]
        center.append(num)
        center.sort()
        return self.findMedian(center)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        if n1 == 0:
            return self.findMedian(nums2)
        if n2 == 0:
            return self.findMedian(nums1)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        if n1 == 1:
            return self.findMedianWithExtra(nums1[0], nums2)
        odd = (n1 + n2) % 2 == 1
        h = (n1 + n2) // 2       # half or smaller half
        i, j = 0, n1 - 1
        while i < j:
            m = i + (j - i) // 2
            m2 = h - m - 2       # by definition, 0 <= m2 <= n2 - 2
            # get mleft, mright s.t. median == (mleft + mright) / 2 or media == mright
            mleft = max(nums1[m], nums2[m2])
            mright = min(nums1[m+1], nums2[m2+1])
            if mleft <= mright:
                return mright if odd else (mleft + mright) / 2
            elif nums1[m] < nums2[m2]:
                i = m + 1
            else:
                j = m
        if i == 0:
            if n1 == n2:         # in this case, h is out of bound for nums2
                return (nums1[0] + nums2[-1]) / 2
            else:
                return min(nums2[h], nums1[0]) if odd else (nums2[h-1] + min(nums1[0], nums2[h])) / 2
        elif i == n1 - 1:
            if n1 == n2:
                return (nums1[-1] + nums2[0]) / 2
            else:
                return nums2[h-n1] if odd else (max(nums1[-1], nums2[h-1-n1]) + nums2[h-n1]) / 2
        else:
            print("Should not reach here")

sol = Solution()
print(sol.findMedianSortedArrays([1,2,3], []))
print(sol.findMedianSortedArrays([], [1,2]))
print(sol.findMedianSortedArrays([4], [1,2]))
print(sol.findMedianSortedArrays([3,4], [1,2]))
print(sol.findMedianSortedArrays([1,3,4], [1,2]))
print(sol.findMedianSortedArrays([3,4,5], [1,2]))
print(sol.findMedianSortedArrays([3,4,5], [6,7]))
print(sol.findMedianSortedArrays([3,4,5], [4,7]))
print(sol.findMedianSortedArrays([3,4,5], [1,4]))
print(sol.findMedianSortedArrays([3,4], [1,2,5]), 3)
