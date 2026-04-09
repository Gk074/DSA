class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        r,c = len(grid), len(grid[0])
        
        def bfs(i,j):
            if i<0 or i>=r or j<0 or j>=c or grid[i][j]!= '1':
                return
            else:
                grid[i][j] = '0'
                bfs(i, j+1)
                bfs(i+1, j)
                bfs(i, j-1)
                bfs(i-1,j)

        num_islands = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1':
                    num_islands +=1
                    bfs(i,j)
        return num_islands