# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        # DFS with stack, attach target number for each node along the way
        stack = [(targetSum, root)]
        while stack:
            target, node = stack.pop()
            target -= node.val
            if not node.left and not node.right and target == 0:
                return True
            if node.right:
                stack.append((target, node.right))
            if node.left:
                stack.append((target, node.left))
        return False