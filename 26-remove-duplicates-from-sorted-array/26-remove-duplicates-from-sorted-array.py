class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev=nums[0]
        ind=1
        for i in range(1,len(nums)):
            if nums[i]==prev:
                continue
            nums[ind]=nums[i]
            prev=nums[i]
            ind+=1
        return (ind)