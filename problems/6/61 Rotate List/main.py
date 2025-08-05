# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        node = head
        count = 1
        while node.next:
            node = node.next
            count += 1
        # here, node is tail
        t = count - k % count
        node.next = head
        for _ in range(t):
            node = node.next
        newhead = node.next
        node.next = None
        return newhead