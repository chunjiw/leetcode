# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, root, level):
        if not root:
            return
        if level > len(self.result) - 1:
            self.result.append(root.val)
        else:
            self.result[level] = max(self.result[level], root.val)
        self.dfs(root.left, level + 1)
        self.dfs(root.right, level + 1)

    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        self.result = []
        self.dfs(root, 0)
        return self.result