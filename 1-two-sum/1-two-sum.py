class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        a=[]
        for i in range(len(nums)):
            x=target-nums[i]
            if x in d:
                a=[d[x],i]
            d[nums[i]]=i
        return a