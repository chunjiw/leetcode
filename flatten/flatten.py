# 114. Flatten Binary Tree to Linked List

# Given a binary tree, flatten it to a linked list in-place.

# For example, given the following tree:

#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
# The flattened tree should look like:

# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        fakeroot = TreeNode(0)
        self.leaf = fakeroot
        self.inplace(root)
        return

    def inplace(self, root):
        if not root:
            return
        left = root.left
        right = root.right
        root.left = None
        root.right = None
        self.leaf.right = root
        self.leaf = root
        self.inplace(left)
        self.inplace(right)
        