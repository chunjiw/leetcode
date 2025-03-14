# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        node = root
        successor = None
        while node:
            if node.val <= p.val:
                node = node.right
            else:
                successor = node
                node = node.left
        return successor