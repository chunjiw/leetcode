# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def tail(self, root):
        while root:
            if not root.right:
                return root
            root = root.right

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        self.flatten(root.left)
        self.flatten(root.right)
        if root.left:
            self.tail(root.left).right = root.right
            root.right = root.left
            root.left = None

        