from typing import List

class Solution:

    def findMedian(self, nums):
        n = len(nums)
        return nums[n//2] if n % 2 == 1 else (nums[n//2-1] + nums[n//2]) / 2

    def findMedianWithExtra(self, num, nums):
        n = len(nums)
        if n == 0:
            return num
        if n == 1:
            return (num + nums[0]) / 2
        if n % 2 == 1:
            sortnum = [num] + nums[n//2-1:n//2+2]
            sortnum.sort()
            return self.findMedian(sortnum)
        else:
            sortnum = [num] + nums[n//2-1:n//2+1]
            sortnum.sort()
            return self.findMedian(sortnum)

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
        isodd = (n1 + n2) % 2 == 1
        half = (n1 + n2) // 2       # half or smaller half
        i, j = 0, n1 - 1
        while i < j:
            m = i + (j - i) // 2
            m2 = half - m - 2       # by definition, m2 <= n2 - 2
            if max(nums1[m], nums2[m2]) <= min(nums1[m+1], nums2[m2+1]):
                return min(nums1[m+1], nums2[m2+1]) if isodd else (max(nums1[m], nums2[m2]) + min(nums1[m+1], nums2[m2+1])) / 2
            elif nums1[m] < nums2[m2]:
                i = m + 1
            else:
                j = m
        if i == 0:
            m2 = half - i - 2       # by definition, m2 <= n2 - 2
            if max(nums1[m], nums2[m2]) <= min(nums1[m+1], nums2[m2+1]):
                return min(nums1[m+1], nums2[m2+1]) if isodd else (max(nums1[m], nums2[m2]) + min(nums1[m+1], nums2[m2+1])) / 2
            elif n1 == n2:
                return (nums1[0] + nums2[-1]) / 2
            else:
                return min(nums2[half], nums1[0]) if isodd else (nums2[half-1] + min(nums1[0], nums2[half])) / 2
        elif i == n1 - 1:
            if n1 == n2:
                return (nums1[-1] + nums2[0]) / 2
            else:
                return nums2[half-n1] if isodd else (max(nums1[-1], nums2[half-1-n1]) + nums2[half-n1]) / 2
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
print(sol.findMedianSortedArrays([3,4], [1,2,5]))
