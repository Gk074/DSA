class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        order = []
        g = defaultdict(list)
        for a,b in prerequisites:
            g[a].append(b)
        UNVISITED, VISITING, VISITED = 0,1,2
        state = [UNVISITED]*numCourses
        def dfs(i):
            if state[i] == VISITING:
                return False
            elif state[i] == VISITED:
                return True
            state[i]= VISITING
            for nei in g[i]:
                if not dfs(nei):
                    return False
            state[i] = VISITED
            order.append(i)
            return True

        for i in range (numCourses):
            if not dfs(i):
                return False
        return True


