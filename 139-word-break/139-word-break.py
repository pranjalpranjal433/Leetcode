class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d={}
        for i in wordDict:
            d[i]=True
        l=len(s)
        dp=[-1]*l
        def find(ind):
            if ind==l:
                return 1
            if dp[ind]!=-1:
                return dp[ind]
            ts=""
            for i in range(ind,l):
                ts+=s[i]
                if ts in d:
                    if find(i+1)==1:
                        dp[ind]=1
                        break
            if dp[ind]==-1:
                dp[ind]=0
            return dp[ind]
        ans=find(0)
        if ans==1:
            return True
        return False