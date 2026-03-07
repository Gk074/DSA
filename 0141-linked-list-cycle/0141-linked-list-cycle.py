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
        seen = set()
        current = head        
        while current:
            if current is None:
                return False
            if current in seen:
                return True
            seen.add(current)
            current = current.next


        