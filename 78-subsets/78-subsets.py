class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        b=[]
        l=len(nums)
        def backtrack(ind,k):
            if len(b)==k:
                ans.append(b[:])
                return
            for i in range(ind,l):
                val=nums[i]
                b.append(val)
                backtrack(i+1,k)
                b.pop()
        for k in range(l+1):
            backtrack(0,k)
        return ans