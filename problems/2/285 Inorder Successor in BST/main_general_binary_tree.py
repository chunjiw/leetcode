# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        if p.right:
            node = p.right
            while node.left:
                node = node.left
            return node
        else:
            found = False
            stack = []
            while root or stack:
                while root:
                    stack.append(root)
                    root = root.left
                root = stack.pop()
                if found:
                    return root
                if root == p:
                    found = True
                root = root.right
