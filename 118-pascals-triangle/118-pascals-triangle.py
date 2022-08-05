class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        a=[]
        ans=[]
        for i in range(numRows):
            b=[]
            for j in range(i+1):
                if j==0 or j==i:
                    b.append(1)
                else:
                    b.append((a[j]+a[j-1]))
            a=b
            ans.append(b)
        return ans