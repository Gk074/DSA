import heapq
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = set(nums)
        if len(n) == 0:
            return 0
        longest=1
        for i in n:
            if i-1 not in n:
                length = 1
                while i+length in n:
                    length+=1
                longest = max(longest, length)
        return longest
        