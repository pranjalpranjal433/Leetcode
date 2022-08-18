class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        b=[]
        ans=[]
        n=len(nums)
        nums.sort()
        def find(st,l):
            if len(b)==l:
                ans.append(b[:])
                return 
            d={}
            for i in range(st,n):
                if nums[i] in d:
                    continue
                d[nums[i]]=1
                b.append(nums[i])
                find(i+1,l)
                b.pop()
        for i in range(n+1):
            find(0,i)
        return ans