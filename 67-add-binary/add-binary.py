class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        bin1 = int(a, 2)
        bin2 = int(b, 2)
        c = bin1+bin2
        return format(c, 'b')

        