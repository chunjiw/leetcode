class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        sums = [0]
        for i in range(k):
            sums[0] += nums[i]
        for i in range(k, len(nums)):
            sums.append(sums[-1] - nums[i-k] + nums[i])
        leftmax = sums.copy()
        leftindex = [0] * len(sums)
        rightmax = sums.copy()
        rightindex = [len(sums) - 1] * len(sums)
        for i in range(1, len(leftmax)):
            if leftmax[i-1] < leftmax[i]:
                leftindex[i] = i
            else:
                leftmax[i] = leftmax[i-1]
                leftindex[i] = leftindex[i-1]
        for i in range(len(rightmax)-2, -1, -1):
            if rightmax[i] >= rightmax[i+1]:
                rightindex[i] = i
            else:
                rightmax[i] = rightmax[i+1]
                rightindex[i] = rightindex[i+1]
        maxsum = 0
        for j in range(k, len(sums)-k):
            curr = leftmax[j-k] + sums[j] + rightmax[j+k]
            if curr > maxsum:
                maxsum = curr
                result = [leftindex[j-k], j, rightindex[j+k]]
        return result
        