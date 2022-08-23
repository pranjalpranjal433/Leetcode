class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        R=n
        C=n
        ans=[]
        b=[]
        for i in range(n):
            sb=[]
            for j in range(n):
                sb.append('.')
            b.append(sb[:])
        def isval(r,c):
            if r<0 or c<0 or r>=R or c>=C:
                return False
            return True
        
        def can_place(r,c):
            for i in range(R):
                if i==r:
                    continue
                if isval(i,c):
                    if b[i][c]=='Q':
                        return False
            for j in range(C):
                if j==C:
                    continue
                if isval(r,j):
                    if b[r][j]=='Q':
                        return False
            for i in range(n):
                if isval(r-i-1,c-i-1):
                    if b[r-i-1][c-i-1]=='Q':
                        return False
                if isval(r+i+1,c+i+1):
                    if b[r+i+1][c+i+1]=='Q':
                        return False
                if isval(r+i+1,c-i-1):
                    if b[r+i+1][c-i-1]=='Q':
                        return False
                if isval(r-i-1,c+i+1):
                    if b[r-i-1][c+i+1]=='Q':
                        return False
            return True
        
        def find(col):
            if col==n:
                c=[]
                for i in b:
                    s=""
                    for j in i:
                        s+=j
                    c.append(s)
                ans.append(c)
                return
            for i in range(n):
                if can_place(i,col):
                    b[i][col]='Q'
                    # print(col,i,b)
                    find(col+1)
                    b[i][col]='.'
                    
        find(0)
        return ans
        
#         ["..Q..","Q....","....Q",".Q...","...Q."],
        
        
#         . . . Q .
#         Q . . . .
#         . . Q . .
#         . . . . Q
#         . Q . . . 
        
        
# . . . Q .
# . Q . . .
# . . . . Q
# Q . . . .
# . . Q . .
        







