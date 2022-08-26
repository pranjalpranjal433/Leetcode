class Solution:
    def countBits(self, n: int) -> List[int]:
        dp=[0]*(n+1)
        if n==0:
            return dp
        dp[1]=1
        for i in range(2,n+1):
            dp[i]=dp[(i>>1)]+dp[i%2]
        return dp