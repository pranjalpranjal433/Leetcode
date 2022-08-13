class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d={}
        d[0]=1
        s=0
        c=0
        for i in nums:
            s+=i
            rem=s%k
            print(s,rem)
            if rem in d:
                c+=d[rem]
                d[rem]+=1
            else:
                d[rem]=1
        return c