# 298. Binary Tree Longest Consecutive Sequence
# DescriptionHintsSubmissionsDiscussSolution
# Given a binary tree, find the length of the longest consecutive sequence path.

# The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

# Example 1:

# Input:

#    1
#     \
#      3
#     / \
#    2   4
#         \
#          5

# Output: 3

# Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
# Example 2:

# Input:

#    2
#     \
#      3
#     / 
#    2    
#   / 
#  1

# Output: 2 

# Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        result = [1]
        streak = [1]
        self.dfs(root, result, streak, float("inf"))
        return result[0]
    
    def dfs(self, node, result, streak, parent):
        if not node:
            return
        if node.val == parent + 1:
            this_streak = streak[0] + 1
            result[0] = max(result[0], this_streak)
        else:
            this_streak = 1
        streak[0] = this_streak
        self.dfs(node.left, result, streak, node.val)
        streak[0] = this_streak
        self.dfs(node.right, result, streak, node.val)
