class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2

            needed_days = 1
            current_weight = 0

            for w in weights:
                if current_weight + w > mid:
                    needed_days += 1
                    current_weight = 0

                current_weight += w

            if needed_days <= days:
                right = mid
            else:
                left = mid + 1

        return left