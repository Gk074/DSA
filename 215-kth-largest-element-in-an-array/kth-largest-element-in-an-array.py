class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        if not nums:
            return 0
        for i in range(len(nums)):
            nums[i] = nums[i]*-1
        n = heapq.heapify(nums)
        for i in range(k):
            c=heapq.heappop(nums)*-1
        return c