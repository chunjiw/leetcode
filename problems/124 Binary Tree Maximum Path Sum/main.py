# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxFrom(self, root):
        if not root:
            return 0
        left = self.maxFrom(root.left)
        right = self.maxFrom(root.right)
        self.result = max(self.result, root.val + left + right)
        return max(0, root.val + max(left, right))

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = -1001
        self.maxFrom(root)
        return self.result
