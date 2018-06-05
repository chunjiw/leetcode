# 515. Find Largest Value in Each Tree Row

# You need to find the largest value in each row of a binary tree.

# Example:
# Input: 

#           1
#          / \
#         3   2
#        / \   \  
#       5   3   9 

# Output: [1, 3, 9]


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if not root:
            return []
        result = []
        level = [root]
        while level:
            maxVal = -float('inf')
            for _ in range(len(level)):
                node = level.pop(0)
                maxVal = max(maxVal, node.val)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            result.append(maxVal)
        return result

