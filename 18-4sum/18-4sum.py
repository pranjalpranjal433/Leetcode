class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        a=[]
        nums.sort()
        k=0
        print(nums)
        while k<len(nums):
            i=k+1
            p=nums[k]
            while i<len(nums):
                x=nums[i]
                l=i+1
                h=len(nums)-1
                while(l<h):
                    nl=nums[l]
                    nh=nums[h]
                    if p+x+nums[l]+nums[h]==target:
                        a.append([p,x,nums[l],nums[h]])
                        while l<h and nums[l]==nl:
                            l+=1
                        while h>i and nums[h]==nh:
                            h-=1
                    elif p+x+nums[l]+nums[h]>target:
                        h-=1
                    else:
                        l+=1
                while i<len(nums) and nums[i]==x:
                    i+=1
            while k<len(nums) and nums[k]==p:
                k+=1
        return a