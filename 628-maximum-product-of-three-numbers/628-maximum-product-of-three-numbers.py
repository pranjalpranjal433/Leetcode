class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums=sorted(nums)
        p=nums[-1]*nums[-2]*nums[-3]
        p1=nums[0]*nums[1]*nums[-1]
        p2=nums[0]*nums[1]*nums[2]
        return max(p,p1,p2)