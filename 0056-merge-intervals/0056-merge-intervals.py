class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # if not intervals:
        #     return []
        # intervals.sort(key = lambda x: x[0])
        # merged = [intervals[0]]
        # for start,end in intervals[1:]:
        #     last_end = merged[-1][1]
        #     if start<=last_end:
        #         merged[-1][1] = max(end, last_end)
        #     else:
        #         merged.append([start,end])
        # return merged

        new=[]
        intervals.sort()
        for i in intervals:
            if not new or i[0]>new[-1][1]:
                new.append(i)
            else:
                end = max(i[1], new[-1][1])
                new[-1][1] = end
        return new

        