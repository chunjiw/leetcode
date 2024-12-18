# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummyhead = ListNode(0, head)
        node = dummyhead
        curr = node.next
        while node.next:
            curr = node.next
            if curr.next and curr.val == curr.next.val:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                node.next = curr.next
            else:
                node = curr
        return dummyhead.next
