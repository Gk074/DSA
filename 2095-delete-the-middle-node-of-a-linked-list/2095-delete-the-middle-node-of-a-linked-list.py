# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode()
        dummy.next = head
        if not head:
            return None
        if not head.next:
            return None
        first = dummy
        second = dummy
        while second.next and second.next.next:
            first = first.next
            second = second.next.next
        first.next = first.next.next
        return head
