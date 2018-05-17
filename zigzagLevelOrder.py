# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        level = [root]
        result = []
        right = True
        while level:
            if not right:
                level.reverse()
                result.append([node.val for node in level])
                level.reverse()
            else:
                result.append([node.val for node in level])
            right = not right
            for i in range(0, len(level)):
                node = level.pop(0)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
        return result
    

