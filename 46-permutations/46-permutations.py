class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=[]
        def find(l):
            if l==n:
                ans.append(nums[:])
                return 
            for i in range(l,n):
                nums[i],nums[l]=nums[l],nums[i]
                find(l+1)
                nums[i],nums[l]=nums[l],nums[i]
        find(0)
        return ans
                