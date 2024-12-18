# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        for _ in range(n):
            first = first.next
        # here, from head to first is n steps
        if not first:
            return head.next
        second = head
        while first.next:
            first = first.next
            second = second.next
        # here, from second to first is n steps. remove second.next
        second.next = second.next.next
        return head
