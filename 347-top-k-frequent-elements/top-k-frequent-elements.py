from collections import Counter
import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        count={}
        for n in nums:
            count[n] = count.get(n,0)+1
        return heapq.nlargest(k, count.keys(), key = count.get)
        
