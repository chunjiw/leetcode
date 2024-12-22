class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        result = [0] * n
        for i in range(n-1, -n, -1):
            num = nums[i]
            while stack and num >= stack[-1]:
                stack.pop()
            result[i] = stack[-1] if stack else -1
            stack.append(num)
        return result