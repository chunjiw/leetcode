"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        node = head
        while node:
            nodecopy = Node(node.val, node.next, node.random)
            node.next = nodecopy
            node = nodecopy.next
        node = head
        while node:
            if node.random:
                node.next.random = node.random.next
            node = node.next.next
        node = head
        while node.next.next:
            copynode = node.next
            nodenext = node.next.next
            copynodenext = node.next.next.next
            copynode.next = copynodenext
            node = nodenext
        return head.next