# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def hasDescendant(self, root, node):
        if not root:
            return False, 1000
        if root == node:
            return True, 0
        atLeft, _ = self.hasDescendant(root.left, node)
        atRight, _ = self.hasDescendant(root.right, node)
        if atLeft:
            return True, -1
        if atRight:
            return True, 1
        return False, 1000

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        _, ploc = self.hasDescendant(root, p)
        _, qloc = self.hasDescendant(root, q)
        if ploc == 0 or qloc == 0 or (ploc + qloc == 0):
            return root
        if ploc + qloc == -2:
            return self.lowestCommonAncestor(root.left, p, q)
        if ploc + qloc == 2:
            return self.lowestCommonAncestor(root.right, p, q)
        