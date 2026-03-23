# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0, head)
        if not head.next:
            return None
        f = dummy
        s=dummy
        for _ in range(n+1):
            s=s.next
        while s:
            f=f.next
            s=s.next
        f.next=f.next.next
        return dummy.next
            

