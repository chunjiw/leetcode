# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Example:

# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:

#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if not root:
            return result
        level = [root]
        while level:
            for i in range(len(level)):
                node = level.pop(0)
                level_value = node.val
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            result.append(level_value)
        return result
