class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nextgreater = dict()
        for num in reversed(nums2):
            while stack and num > stack[-1]:
                stack.pop()
            if not stack:
                nextgreater[num] = -1
            else:
                nextgreater[num] = stack[-1]
            stack.append(num)
        return [nextgreater[num] for num in nums1]
