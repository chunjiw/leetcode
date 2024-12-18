# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        head1 = ListNode(0)
        head2 = ListNode(0)
        node, node1, node2 = head, head1, head2
        while node:
            if node.val < x:
                node1.next = node
                node1 = node
            else:
                node2.next = node
                node2 = node
            node = node.next
        node1.next = head2.next
        node2.next = None
        return head1.next
