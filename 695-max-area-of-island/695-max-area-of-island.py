class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        def isval(i,j):
            if i<0 or i>=r or j<0 or j>=c:
                return False
            return True
        def count(i,j):
            if isval(i,j)==False or grid[i][j]==0:
                return 0
            p=1 if grid[i][j]==1 else 0
            grid[i][j]=0
            up=count(i-1,j)
            left=count(i,j-1)
            right=count(i+1,j)
            down=count(i,j+1)
            
            return up+left+right+down+p
        ans=0
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    ans=max(ans,count(i,j))
        return ans
        