class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans=inf
        c=0
        print(nums)
        for i in range(len(nums)):
            l=i+1
            h=len(nums)-1
            while(l<h):
                s=nums[i]+nums[l]+nums[h]
                x=target-s
                if s==target:
                    return target
                if s<target:
                    l+=1
                else:
                    h-=1
                if ans>abs(x):
                    ans=abs(x)
                    c=s;
        return c