class Solution:
    def numDecodings(self, s: str) -> int:
        d={}
        for i in range(1,27):
            d[str(i)]=True
        def isVal(num):
            if num in d:
                return True
            return False
        l=len(s)
        dp=[0]*(l+1)
        dp[0]=1
        dp[1]=1 if isVal(s[0]) else 0
        for i in range(2,l+1):
            if isVal(s[i-1]):
                dp[i]+=dp[i-1]
            if isVal((s[i-2]+s[i-1])):
                dp[i]+=dp[i-2]
            if dp[i]==0:
                break
        return dp[l]