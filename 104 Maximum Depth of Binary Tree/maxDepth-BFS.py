# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        line = [root]
        next = []
        depth = 0
        while line:
            n = line.pop()
            if n.left:
                next.append(n.left)
            if n.right:
                next.append(n.right)
            if not line:
                line = next
                next = []
                depth += 1
        return depth
            