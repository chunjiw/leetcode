"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


from collections import deque
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        queue = deque([node])
        root = Node(node.val)
        cloned = {node.val: (node, root)}
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                for neighbor in node.neighbors:
                    if neighbor.val not in cloned:
                        queue.append(neighbor)
                        cloned[neighbor.val] = (neighbor, Node(neighbor.val))
        for node, nodecopy in cloned.values():
            for neighbor in node.neighbors:
                nodecopy.neighbors.append(cloned[neighbor.val][1])
        return root