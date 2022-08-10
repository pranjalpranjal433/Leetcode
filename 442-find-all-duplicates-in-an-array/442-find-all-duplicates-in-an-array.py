class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        k=len(nums)
        for i in nums:
            x=abs(i)%k-1
            nums[x]+=k
        a=[]
        for i in range(len(nums)):
            if nums[i]>2*k:
                a.append(i+1)
        return a