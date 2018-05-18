# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# 111. Minimum Depth of Binary Tree

# Note: A leaf is a node with no children.

# Example:

# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its minimum depth = 2.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.res = float('inf')
        self.dfs(root, 0)
        return self.res

    def dfs(self, root, level):
        level += 1
        if level > self.res:
            return
        if not root.left and not root.right:
            self.res = min(self.res, level)
            return
        if root.left:
            self.dfs(root.left, level)
        if root.right:
            self.dfs(root.right, level)
        return
