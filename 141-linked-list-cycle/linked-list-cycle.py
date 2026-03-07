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
        if not head or not head.next:
            return False
        one, two = head, head.next
        while two and two.next:
            if(one==two):
                return True
            one = one.next
            two = two.next.next
        return False

        