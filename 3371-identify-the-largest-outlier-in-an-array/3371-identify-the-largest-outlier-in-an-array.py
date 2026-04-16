class Solution(object):
    def getLargestOutlier(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        total = sum(nums)
        out = float('-inf')
        freq = Counter(nums)
        for i in nums:
            remaining = total - i
            if remaining % 2 != 0:
                continue
            x = remaining//2
            freq[i]-=1

            if freq[x]>0:
                out = max(out, i)
            freq[i]+=1
        return out
