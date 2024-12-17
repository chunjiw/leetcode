# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        node = root
        heritage = 0
        stack = []
        result = 0
        while node:
            heritage = heritage * 10 + node.val
            if node.left and node.right:
                stack.append((node.right, heritage))
                node = node.left
            elif node.left:
                node = node.left
            elif node.right:
                node = node.right
            else:
                result += heritage
                if not stack:
                    return result
                else:
                    node, heritage = stack.pop()
