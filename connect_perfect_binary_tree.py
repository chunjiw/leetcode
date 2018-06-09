# 116. Populating Next Right Pointers in Each Node
# DescriptionHintsSubmissionsDiscussSolution
# Given a binary tree

# struct TreeLinkNode {
#   TreeLinkNode *left;
#   TreeLinkNode *right;
#   TreeLinkNode *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.

# Note:

# You may only use constant extra space.
# Recursive approach is fine, implicit stack space does not count as extra space for this problem.
# You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
# Example:

# Given the following perfect binary tree,

#      1
#    /  \
#   2    3
#  / \  / \
# 4  5  6  7
# After calling your function, the tree should look like:

#      1 -> NULL
#    /  \
#   2 -> 3 -> NULL
#  / \  / \
# 4->5->6->7 -> NULL



# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    # recursively connect
    def connect(self, root):
        if not root:
            return
        self.helper(root.left, root.right)
    
    def helper(self, left, right):
        if not left or not right:
            return
        left.next = right
        self.helper(left.left, left.right)
        self.helper(right.left, right.right)
        self.helper(left.right, right.left)
        
