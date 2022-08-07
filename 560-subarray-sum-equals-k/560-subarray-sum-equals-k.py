class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d={}
        d[0]=1
        s=0
        c=0
        for i in nums:
            s+=i
            if (s-k) in d:
                c+=d[(s-k)]
            d[s]=d[s]+1 if s in d else 1
        return c
            