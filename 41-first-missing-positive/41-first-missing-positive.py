class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i]=0 if nums[i]<0 else nums[i]
        for i in nums:
            x=abs(i)-1
            if x>=0 and x<len(nums):
                nums[x]=-nums[x] if nums[x]>0 else nums[x]
                if nums[x]==0:
                    nums[x]=-len(nums)
        for i in range(len(nums)):
            if nums[i]>=0:
                return i+1
        return len(nums)+1
            