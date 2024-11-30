# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        fakeroot = TreeNode(0, None, root)
        result, stack = [], [fakeroot]
        while stack:
            # At start of each iteration, gaurantee node.left is None or in the stack
            node = stack.pop()
            result.append(node.val)
            node = node.right
            while node:
                stack.append(node)
                node = node.left
        return result[1:]