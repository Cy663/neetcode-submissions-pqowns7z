class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R,C = len(grid),len(grid[0])
        visit = set()
        def dfs(r,c):
            if (r,c) not in visit and 0<=r<R and 0<=c<C and grid[r][c]==1:
                visit.add((r,c))
                return 1+dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1)
            else:
                return 0
        res = 0
        for r in range(R):
            for c in range(C):
                res = max(res,dfs(r,c))
        return res