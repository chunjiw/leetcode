# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, 0)])
        result = 0
        while queue:
            for _ in range(len(queue)):
                node, heritage = queue.popleft()
                value = heritage * 10 + node.val
                if node.left:
                    queue.append((node.left, value))
                if node.right:
                    queue.append((node.right, value))
                if not node.left and not node.right:
                    result += value
        return result