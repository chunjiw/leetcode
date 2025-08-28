# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def upsideDownBinaryTree(self, root: TreeNode | None) -> TreeNode | None:
        
        if not root or (not root.left and not root.right):
            return root

        left = root.left
        right = root.right

        newroot = self.upsideDownBinaryTree(left)
        left.left, left.right = right, root
        root.left = root.right = None
        
        return newroot