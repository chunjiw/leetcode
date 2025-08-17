# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        fakehead = ListNode(0, head)
        head = fakehead
        hi = 0    # head index
        # head -> node1 -> node2
        # head <- node1    node2
        #          head -> node1 -> node2
        node1 = head.next
        while head:
            node2 = node1.next if node1 else None
            if left - 1 == hi:
                leftBound = head
                startNode = node1
            elif left - 1 < hi < right:
                node1.next = head
            elif hi == right:
                leftBound.next = head
                startNode.next = node1
                break
            head = node1
            node1 = node2
            hi += 1
        return fakehead.next

        