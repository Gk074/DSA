class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in h:
                return [h[diff],i]
            h[n]=i
        return[]
    