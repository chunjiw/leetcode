# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:

    def reverse(self, left, right, level):
        if level % 2 == 0:
            left.val, right.val = right.val, left.val
            self.reverse(left.left, right.right, level + 1)
            self.reverse(left.right, right.left)

    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.reverse(root.left, root.right, 0)
        return root

    def reverseOddLevels_BFS(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])
        level = 0
        while queue:
            if level % 2:
                for i in range(len(queue) // 2):
                    queue[i].val, queue[-i-1].val = queue[-i-1].val, queue[i].val
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    queue.append(node.right)
            level += 1
        return root