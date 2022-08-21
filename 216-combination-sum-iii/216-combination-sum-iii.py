class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        b=[]
        ans=[]
        
        def find(l,s,st):
            if l==0 and s==0:
                ans.append(b[:])
                return 
            if l==0 or s<=0:
                return
            for i in range(st,10):
                b.append(i)
                find(l-1,s-i,i+1)
                b.pop()
        find(k,n,1)
        return ans