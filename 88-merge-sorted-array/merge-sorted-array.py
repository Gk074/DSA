class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        mmid = m-1
        nlast = n-1
        mright = m+n-1
        while nlast>=0:
            if mmid>=0 and nums1[mmid] > nums2[nlast]:
                nums1[mright] = nums1[mmid]
                mmid -=1
            else:
                nums1[mright] = nums2[nlast]
                nlast-=1
            mright-=1