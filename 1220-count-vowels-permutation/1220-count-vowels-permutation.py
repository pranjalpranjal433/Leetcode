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
            for j in range(5):
                if j==0:
                    x[j]=(dp[1]+dp[2]+dp[4])%mod
                elif j==1:
                    x[j]=(dp[0]+dp[2])%mod
                elif j==2:
                    x[j]=(dp[1]+dp[3])%mod
                elif j==3:
                    x[j]=(dp[2])%mod
                elif j==4:
                    x[j]=(dp[2]+dp[3])%mod
            dp=x[:]
        return (sum(dp)%mod)
#         a = 1
#         e = 1
#         i = 1
#         o = 1
#         u = 1
#         mod = pow(10, 9)+7;
        
#         for j in range(1,n):
#             a2 = (e + i + u) % mod;
#             e2 = (a + i) % mod;
#             i2 = (e + o) % mod;
#             o2 = i;
#             u2 = (o + i) % mod;
#             a = a2
#             e = e2
#             i = i2
#             o = o2
#             u = u2;
#             print(a,e,i,o,u)
        
#         return (a + e + i + o + u) % mod;