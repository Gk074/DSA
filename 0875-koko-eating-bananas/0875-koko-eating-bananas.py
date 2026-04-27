class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        left = 1
        right = max(piles)

        while left < right:
            k = (left + right) // 2

            hours = 0
            for pile in piles:
                hours += (pile + k - 1) // k   # same as ceil(pile / k)

            if hours <= h:
                right = k   # k works, try smaller speed
            else:
                left = k + 1  # k too slow, need bigger speed

        return left        