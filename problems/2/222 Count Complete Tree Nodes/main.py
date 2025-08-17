# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def getNode(self, root, path, h):
        while h > 1:
            root = root.left if path // 2**(h-2) == 0 else root.right
            path %= 2**(h-2)
            h -= 1
        return root

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        node = root
        h = 0
        while node:
            node = node.left
            h += 1
        bottomlen = 2 ** (h-1)
        i, j = 0, bottomlen - 1
        while i < j:
            m = (i + j) // 2
            if self.getNode(root, m, h):
                i = m + 1
            else:
                j = m
        if self.getNode(root, i, h):
            return bottomlen + i
        else:
            return bottomlen - 1 + i