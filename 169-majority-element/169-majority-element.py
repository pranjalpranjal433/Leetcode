class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c=0
        m=nums[0]
        for i in nums:
            if c==0:
                c=1
                m=i 
            else:
                if i==m:
                    c+=1
                else:
                    c-=1
        return m
            