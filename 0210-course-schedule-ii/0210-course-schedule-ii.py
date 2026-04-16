class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        d=defaultdict(list)
        order=[]
        for i,j in prerequisites:
            d[i].append(j)
        VISITED, VISITING, UNVISITED = 2,1,0
        state = [UNVISITED]*numCourses
        def dfs(i):
            if state[i]==VISITING:
                return False
            elif state[i] == VISITED:
                return True
            state[i]=VISITING
            
            for nei in d[i]:
                if not dfs(nei):
                    return True
            state[i]=VISITED
            order.append(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return order
        