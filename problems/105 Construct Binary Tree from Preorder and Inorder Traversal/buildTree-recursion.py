from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root_index = inorder.index(preorder[0])
        left = self.buildTree(preorder[1 : 1+root_index], inorder[:root_index])
        right = self.buildTree(preorder[1 + root_index:], inorder[1 + root_index:])
        root = TreeNode(preorder[0], left, right)
        return root
