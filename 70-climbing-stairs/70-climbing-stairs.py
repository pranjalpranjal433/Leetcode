class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=1:
            return n
        a=1
        b=1
        ans=0
        for i in range(2,n+1):
            ans=a+b
            a=b
            b=ans
        return ans
            