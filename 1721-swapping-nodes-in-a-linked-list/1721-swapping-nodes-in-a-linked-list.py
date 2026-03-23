# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        t = head
        for _ in range(k-1):
            t = t.next
        p1 = t
        p2 = head   
        while t.next:
            t = t.next
            p2 = p2.next
            
        p1.val,p2.val = p2.val, p1.val
        return head
