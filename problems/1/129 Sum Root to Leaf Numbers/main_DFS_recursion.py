# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def dfs(self, root, heritage):
        value = heritage * 10 + root.val
        if not root.left and not root.right:
            self.result += value
        if root.left:
            self.dfs(root.left, value)
        if root.right:
            self.dfs(root.right, value)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        self.dfs(root, 0)
        return self.result