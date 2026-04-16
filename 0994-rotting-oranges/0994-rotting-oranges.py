from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row,column = len(grid), len(grid[0])
        fresh = 0
        minutes=0
        q=deque()
        for i in range(row):
            for j in range(column):
                if grid[i][j]==2:
                    q.append((i,j,0))
                if grid[i][j]==1:
                    fresh+=1
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while q and fresh>0:
            r,c = q.popleft()
            for dr,dc in directions:
                nr,nc = r+dr, c+dc
                if 0<=nr<row and 0<=nc<column and grid[nr][nc]==1:
                    grid[nr][nc]=2
                    fresh-=1
                    q.append((nr,nc, minutes+=1))
        return minutes if fresh==0 else -1
