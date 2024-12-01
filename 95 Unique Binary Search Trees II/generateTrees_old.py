# 95. Unique Binary Search Trees II
# DescriptionHintsSubmissionsDiscussSolution
# Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

# Example:

# Input: 3
# Output:
# [
#   [1,null,3,2],
#   [3,2,null,1],
#   [3,1,null,null,2],
#   [2,1,3],
#   [1,null,2,null,3]
# ]
# Explanation:
# The above output corresponds to the 5 unique BST's shown below:

#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        # approach: recursively contruct tree
        if n == 0:
            return []
        return self.helper(range(1, n + 1))
    
    def helper(self, nums):
        result = []
        if not nums:
            return [None]
        for i in range(0, len(nums)):
            all_left = self.helper(nums[0:i])
            all_right = self.helper(nums[i + 1:len(nums)])
            for left in all_left:
                for right in all_right:
                    root = TreeNode(nums[i])
                    root.left = left
                    root.right = right
                    result.append(root)
        return result
        
