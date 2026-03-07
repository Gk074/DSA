# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from collections import deque
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        seen = set()
        current = head
        if current in seen:
            return True
        
        while current:
            if current in seen:
                return True
            else:
                seen.add(current)
            current = current.next
        return False


        