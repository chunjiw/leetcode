# From right to left, if element is not smaller than top of stack, push number in stack;
# so we are keeping a monotonically increasing stack.
# If current element is smaller than top of stack, pop the stack until element is bigger than top of stack.
# The last popped number should swap with current element.

class Solution:

    def reverse(self, nums, i):
        x, y = i + 1, len(nums) - 1
        while x < y:
            nums[x], nums[y] = nums[y], nums[x]
            x += 1
            y -= 1

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        stack = [n-1]
        for i in range(n-2, -1, -1):
            if nums[i] >= nums[i+1]:
                stack.append(i)
            else:
                while stack and nums[i] < nums[stack[-1]]:
                    k = stack.pop()    # nums[k] is the smallest number that is bigger than nums[i]
                # here, should swap i and k, then reverse everything after i
                # because after i, the number is monotonically decreasing
                nums[i], nums[k] = nums[k], nums[i]
                self.reverse(nums, i)
                return
        nums.reverse()