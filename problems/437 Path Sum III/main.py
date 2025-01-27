# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, node, history, currsum):
        if not node:
            return
        currsum += node.val
        if currsum - self.target in history:
            self.result += history[currsum - self.target]
        history[currsum] = history.get(currsum, 0) + 1
        self.dfs(node.left, history, currsum)
        self.dfs(node.right, history, currsum)
        history[currsum] -= 1
        if history[currsum] == 0:
            del history[currsum]
        currsum -= node.val

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.target= targetSum
        self.result = 0
        self.dfs(root, {0:1}, 0)
        return self.result