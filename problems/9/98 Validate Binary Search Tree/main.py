# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isValid(self, root, leftbound, rightbound):
        if not root:
            return True
        if root.val <= leftbound or rightbound <= root.val:
            return False
        return self.isValid(root.left, leftbound, root.val) and self.isValid(root.right, root.val, rightbound)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root, -float("inf"), float('inf'))
        