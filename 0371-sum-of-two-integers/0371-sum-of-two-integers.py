class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        while b!=0:
            c = ((a&b)<<1) & MASK
            a = (a^b) & MASK
            b=c
        return a if a <= MAX_INT else ~(a ^ MASK)