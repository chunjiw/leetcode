# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummyhead = ListNode(0, head)
        node = dummyhead
        while node.next:
            first = second = node.next
            for _ in range(k - 1):
                first = first.next
                if not first:
                    return dummyhead.next
            # here, second -> .. -> first needs to be reversed
            future = first.next
            # reverse within
            prev = second
            curr = second.next
            for _ in range(k - 1):
                nex = curr.next
                curr.next = prev
                prev = curr
                curr = nex
            # link this chunk
            node.next = first
            second.next = future
            node = second
        return dummyhead.next