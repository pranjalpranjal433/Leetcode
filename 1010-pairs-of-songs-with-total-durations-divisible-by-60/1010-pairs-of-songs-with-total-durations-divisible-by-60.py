class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        d={}
        c=0
        for i in time:
            x=i%60
            p=(60-x) if x!=0 else 0
            if p in d:
                c+=d[p]
            d[x]=d[x]+1 if x in d else 1
        return c