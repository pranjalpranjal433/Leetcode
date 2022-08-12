class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R=len(board)
        C=len(board[0])
        p=set()
        lw=len(word)
        def find(r,c,s):
            if  r<0 or c<0 or r==R or c==C or ((r,c) in p) or board[r][c]!=word[s]:
                return False
            if s==lw-1:
                return True
            p.add((r,c))
            x=find(r+1,c,s+1) or find(r-1,c,s+1) or find(r,c+1,s+1) or find(r,c-1,s+1)
            if x:
                return True
            p.remove((r,c))
        for i in range(R):
            for j in range(C):
                if find(i,j,0):
                    return True
        return False
            