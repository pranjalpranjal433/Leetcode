class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        b=[]
        ans=[]
        def find(l):
            if len(b)==k:
                ans.append(b[:])
                return 
            for i in range(l,n):
                b.append(i+1)
                find(i+1)
                b.pop()
        find(0)
        return ans