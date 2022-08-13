class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # d={}
        # d['']=['a','e','i','o','u']
        # d['a']=['e']
        # d['e']=['a','i']
        # d['i']=['a','e','o','u']
        # d['o']=['i','u']
        # d['u']=['a']
        # d['ans']=0
        # mod=10**9+7
        # def find(l,ls):
        #     if l==n:
        #         d['ans']+=1
        #         d['ans']=d['ans']%mod
        #         return
        #     for i in d[ls]:
        #         find(l+1,i)
        # find(0,'')
        # return d['ans']
        dp=[1]*5
        x=[1]*5
        mod=10**9+7
        for i in range(1,n):
            x[0]=(dp[1]+dp[2]+dp[4])%mod
            x[1]=(dp[0]+dp[2])%mod
            x[2]=(dp[1]+dp[3])%mod
            x[3]=(dp[2])%mod
            x[4]=(dp[2]+dp[3])%mod
            dp=x[:]
        return (sum(dp)%mod)
