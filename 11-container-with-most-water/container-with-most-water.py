class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        end = len(height)-1
        c = 0
        while start<end:
            l = end - start
            carry = l*min(height[start],height[end])
            c = max(c,carry)
            if height[start]<height[end]:
                start+=1
            else:
                end-=1
        return c

