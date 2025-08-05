# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        result = []
        while queue:
            line = []
            for _ in range(len(queue)):
                n = queue.pop(0)
                line.append(n.val)
                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)
            result.append(line)
        return result