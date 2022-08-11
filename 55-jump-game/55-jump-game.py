class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        if nums[0]==0:
            return False
        val=nums[0]
        for i in nums:
            if val<0:
                return False
            if i>val:
                val=i;
            val-=1
        return True
            