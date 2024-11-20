# 4. Median of Two Sorted Arrays
# DescriptionHintsSubmissionsDiscussSolution
# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# Example 1:
# nums1 = [1, 3]
# nums2 = [2]

# The median is 2.0
# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not nums1:
            return self.findMedian(nums2)
        if not nums2:
            return self.findMedian(nums1)
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        # when there's no overlap
        if nums1[-1] <= nums2[0]:
            return self.findMedian(nums1 + nums2)
        if nums2[-1] <= nums1[0]:
            return self.findMedian(nums2 + nums1)
        # binary search
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        while left < right - 1:
            i = (left + right) / 2
            j = (m + n) / 2 - i
            if (j == 0 or i == m or nums2[j - 1] <= nums1[i]) and \
                (i == 0 or j == n or nums1[i - 1] <= nums2[j]):
                return self.findMedian2(nums1, nums2, i, j)
            elif j == 0 or i == m or nums2[j - 1] > nums1[i]:
                left = i
            else:
                right = i
        i = left
        j = (m + n) / 2 - i
        if (j == 0 or i == m or nums2[j - 1] <= nums1[i]) and \
            (i == 0 or j == n or nums1[i - 1] <= nums2[j]):
            return self.findMedian2(nums1, nums2, i, j)
        else:
            return self.findMedian2(nums1, nums2, i + 1, j - 1)
    

    def findMedian2(self, nums1, nums2, i, j):
        odd = (len(nums1) + len(nums2)) % 2
        if j == 0 or j == len(nums2):
            return self.findMedian2(nums2, nums1, j, i)
        # if i == 0:
        #     return self.findMiddle(nums2, nums1)
        # if i == len(nums1):
        #     return self.findMiddle(nums1, nums2)
        if odd:
            if i == len(nums1):
                return nums2[j]
            else:
                return min(nums1[i], nums2[j])
        else:
            if i == len(nums1):
                return float(nums2[j] + max(nums1[i - 1], nums2[j - 1])) / 2
            if i == 0:
                return float(min(nums1[i], nums2[j]) + nums2[j - 1]) / 2
            return float(min(nums1[i], nums2[j]) + max(nums1[i - 1], nums2[j - 1])) / 2

    def findMedian(self, nums):
        if not nums:
            return None
        n = len(nums)
        if not n % 2:
            return float(nums[n/2 - 1] + nums[n/2]) / 2
        else:
            return nums[n/2]