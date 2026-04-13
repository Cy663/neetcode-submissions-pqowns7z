class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R,C = len(grid),len(grid[0])
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        self.res = 0
        def dfs(r,c,first):
            if 0<=r<R and 0<=c<C and grid[r][c]=="1":
                grid[r][c]="0"
                if first:
                    self.res+=1
                for d in dirs:
                    dfs(r+d[0],c+d[1],False)
            else:
                return
        for r in range(R):
            for c in range(C):
                dfs(r,c,True)
        return self.res