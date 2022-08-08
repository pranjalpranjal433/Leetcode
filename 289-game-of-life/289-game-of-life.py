class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def neigh(r,c,R,C):
            a=0
            for i in range(r-1,r+2):
                for j in range(c-1,c+2):
                    if((i==r and j==c) or i<0 or j<0 or i==R or j==C):
                        continue
                    if board[i][j] in [1,3]:
                        a+=1
            return a
        for i in range(len(board)):
            for j in range(len(board[0])):
                cntn=neigh(i,j,len(board),len(board[0]))
                if board[i][j]:
                    if cntn in [2,3]:
                        board[i][j]=3
                elif cntn==3:
                    board[i][j]=2
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==1:
                    board[i][j]=0
                elif board[i][j] in [2,3]:
                    board[i][j]=1
        
            