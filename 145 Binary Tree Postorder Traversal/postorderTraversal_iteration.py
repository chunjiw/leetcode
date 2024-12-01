# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result, stack = [], [root]
        peeked = set()
        while stack:
            node = stack[-1]
            if node in peeked:
                result.append(node.val)
                stack.pop()
            else:
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
                peeked.add(node)
        return result
            