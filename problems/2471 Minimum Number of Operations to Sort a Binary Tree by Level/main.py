# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional

from collections import deque

class Solution:

    def operations(self, nums):
        index = dict()
        for i, n in enumerate(nums):
            index[n] = i
        sorted_nums = sorted(nums)
        result = 0
        for i in range(len(nums)):
            n = nums[i]
            if n != sorted_nums[i]:
                j = index[sorted_nums[i]]   # nums[j] should be at index i
                nums[i], nums[j] = nums[j], nums[i]
                index[n] = j
                index[sorted_nums[i]] = i   # unnecessary
                result += 1
        return result

    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        ans = 0
        while queue:
            line = []
            for _ in range(len(queue)):
                node = queue.popleft()
                line.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans += self.operations(line)
        return ans

sol = Solution()
# print(sol.operations([1,2,3]))
# print(sol.operations([2,1,3]))
# print(sol.operations([3,2,1]))
# print(sol.operations([3,1,2]))
# print(sol.operations([4,3]))
print(sol.operations([7,6,8,5]))