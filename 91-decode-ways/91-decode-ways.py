class Solution:
    def numDecodings(self, s: str) -> int:
        d={}
        for i in range(1,27):
            d[str(i)]=True
        def isVal(num):
            if num in d:
                return True
            return False
        c=[0]
        l=len(s)
        dp=[-1]*(l+1)
        dp[l]=1
        def find(ind):
            if ind==l:
                return dp[l]
            if dp[ind]!=-1:
                return dp[ind]
            one = s[ind]
            dp[ind]=0
            if isVal(one):
                dp[ind]=find(ind+1)
            if ind<(l-1):
                two = s[ind]+s[ind+1]
                if isVal(two):
                        dp[ind]+=find(ind+2)
            return dp[ind]
        dp[0]=find(0)
        dp[0]=dp[0] if dp[0]>-1 else 0
        return dp[0]