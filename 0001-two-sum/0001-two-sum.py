class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) is 0:
            return 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                current = nums[i]+ nums[j]
                if current==target:
                    return[i,j]
    