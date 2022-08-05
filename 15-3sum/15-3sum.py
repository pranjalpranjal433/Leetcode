class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        a=[]
        nums.sort()
        i=0
        while i<len(nums):
            x=nums[i]
            l=i+1
            h=len(nums)-1
            while(l<h):
                nl=nums[l]
                nh=nums[h]
                if x+nums[l]+nums[h]==0:
                    a.append([x,nums[l],nums[h]])
                    while l<h and nums[l]==nl:
                        l+=1
                    while h>i and nums[h]==nh:
                        h-=1
                elif x+nums[l]+nums[h]>0:
                    h-=1
                else:
                    l+=1
            while i<len(nums) and nums[i]==x:
                i+=1
        return a