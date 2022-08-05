class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind=0
        for i in range(len(nums)):
            if nums[i]==0:
                continue
            nums[ind]=nums[i]
            ind+=1
        while(ind<len(nums)):
            nums[ind]=0
            ind+=1
        