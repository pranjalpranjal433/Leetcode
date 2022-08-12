class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        val=nums[0]
        j=0
        res=0
        for i in range(1,len(nums)-1):
            val-=1
            if val>=0:
                res=max(res,nums[i]-val)
            if val==0:
                j+=1
                val=res
                res=0
        j+=1
        return j
            