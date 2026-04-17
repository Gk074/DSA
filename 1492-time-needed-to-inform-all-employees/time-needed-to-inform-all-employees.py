import math
from collections import defaultdict
class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        d = defaultdict(list)
        for i in range(n):
            if manager[i]!=-1:
                d[manager[i]].append(i)
        def dfs(i):
            if i not in d:
                return 0
            time=0
            for nei in d[i]:
                time = max(time,dfs(nei))
            return informTime[i]+time

        return dfs(headID)
            
