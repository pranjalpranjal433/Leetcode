class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        nr=len(matrix)-1
        nc=len(matrix[0])-1        
        top=0
        bottom=nr
        left=0
        right=nc
        d=0
        a=[]
        while top<=bottom and left<=right:
            d=d%4
            if d==0:
                for i in range(left,right+1):
                    a.append(matrix[top][i])
                top+=1
                d+=1
            elif d==1:
                for i in range(top,bottom+1):
                    a.append(matrix[i][right])
                right-=1
                d+=1
            elif d==2:
                for i in range(right,left-1,-1):
                    a.append(matrix[bottom][i])
                bottom-=1
                d+=1
            else:
                for i in range(bottom,top-1,-1):
                    a.append(matrix[i][left])
                left+=1
                d+=1
        return a