"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue = deque([root])
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                node.next = queue[0] if i < n - 1 else None
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root