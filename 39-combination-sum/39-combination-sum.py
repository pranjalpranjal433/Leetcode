class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        a=[]
        def find(i,l,s,b):
            if i==l or s>=target:
                if s==target:
                    a.append(b)
                return
            find(i+1,l,s,b)
            find(i,l,s+candidates[i],b+[candidates[i]])
        find(0,len(candidates),0,[])
        return a
            
            