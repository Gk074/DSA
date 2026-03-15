import math
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        mf=math.factorial(m-1)
        nf=math.factorial(n-1)
        c=(m+n)-2
        val = math.factorial(c)/(mf*nf)
        return val
        