# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head

        prevGroup = dummy

        while True:

            kth = prevGroup

            # check if k nodes exist
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            nextGroup = kth.next

            prev = nextGroup
            curr = prevGroup.next

            # reverse current group
            while curr != nextGroup:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            temp = prevGroup.next

            prevGroup.next = kth
            prevGroup = temp