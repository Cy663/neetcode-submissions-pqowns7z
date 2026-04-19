class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R,C = len(grid),len(grid[0])
        def dfs(r,c):
            if 0<=r<R and 0<=c<C and grid[r][c]=="1":
                grid[r][c] = "0"
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)
        count = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c]=="1":
                    count+=1
                    dfs(r,c)
        return count