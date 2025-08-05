# 42. Trapping Rain Water
# DescriptionHintsSubmissionsDiscussSolution
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.



class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 3:
            return 0
        rightward, leftward = [0 for _ in range(len(height))], [0 for _ in range(len(height))]

        leftMax, rightMax = 0, 0

        for i in range(len(height)):
            if leftMax <= height[i]:
                leftMax = height[i]
            else:
                rightward[i] = leftMax - height[i]
            if height[-i-1] >= rightMax:
                rightMax = height[-i-1]
            else:
                leftward[-i-1] = rightMax - height[-i-1]

        result = 0
        for i in range(len(height)):
            result += min(rightward[i], leftward[i])

        return result


