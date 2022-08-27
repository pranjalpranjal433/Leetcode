import math
class Solution:
    def divisorGame(self, n: int) -> bool:
        dp=[-1]*1001
        dp[1]=0
        def find(n):
            if dp[n]!=-1:
                return dp[n]
            p=math.sqrt(n)
            p=((int)(p))+1
            for i in range(1,p):
                if (n%i==0):
                    if find(n-i)==0:
                        dp[n]=1
                        return 1
                    if i!=1 and find(n-(n//i))==0:
                        dp[n]=1
                        return 1
            dp[n]=0
            return 0
        # return find(n)
        return n%2==0