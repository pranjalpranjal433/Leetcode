class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        R=len(image)
        C=len(image[0])
        oc=image[sr][sc]
        if oc==color:
            return image
        def isval(i,j):
            if i<0 or j<0 or i>=R or j>=C or image[i][j]!=oc:
                return True
            return False
        def fill(i,j):
            if isval(i,j)==False:
                image[i][j]=color
                fill(i+1,j)
                fill(i-1,j)
                fill(i,j-1)
                fill(i,j+1)
        fill(sr,sc)
        return image
            
        