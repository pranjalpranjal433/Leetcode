class Solution:
    def myPow(self, x: float, n: int) -> float:
        def myPoww(x,n):
            if n==1:
                return x
            if n==0:
                return 1
            p=myPoww(x,n//2)
            ans=p*p
            if n%2!=0:
                ans=ans*x
            return ans
        if n<0:
            return 1.0/myPoww(x,abs(n))
        return myPoww(x,n)
    