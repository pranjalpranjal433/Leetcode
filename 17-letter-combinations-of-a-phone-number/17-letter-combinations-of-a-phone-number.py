class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d={}
        d["2"]=['a','b','c']
        d["3"]=['d','e','f']
        d["4"]=['g','h','i']
        d["5"]=['j','k','l']
        d["6"]=['m','n','o']
        d["7"]=['p','q','r','s']
        d["8"]=['t','u','v']
        d["9"]=['w','x','y','z']
        
        l=len(digits)
        if l==0:
            return []
        ans=[]
        def find(st,b):
            if len(b)==l:
                ans.append(b)
                return 
            for i in d[digits[st]]:
                b1=b+i
                find(st+1,b1)
        
        find(0,"")
        
        return ans