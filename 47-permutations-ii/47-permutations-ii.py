class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=[]
        def find(l):
            if l==n:
                ans.append(nums[:])
                return 
            d=set()
            for i in range(l,n):
                if nums[i] not in d:
                    d.add(nums[i])
                    nums[i],nums[l]=nums[l],nums[i]
                    find(l+1)
                    nums[i],nums[l]=nums[l],nums[i]
        find(0)
        return ans