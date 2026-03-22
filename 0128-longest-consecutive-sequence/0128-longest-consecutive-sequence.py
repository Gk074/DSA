import heapq
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = sorted(nums)
        l=len(nums)
        longest = 1
        c=1
        if l == 0:
            return 0
        for i in range(l-1):
            if n[i] == n[i+1]:
                continue
            if n[i]+1 == n[i+1]:
                c+=1
            else:
                longest = max(longest,c)
                c = 1
        return max(longest, c)
        