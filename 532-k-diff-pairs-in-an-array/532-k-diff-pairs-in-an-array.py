class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        d={}
        d[nums[0]]=1
        c=0
        m={}
        for i in range(1,len(nums)):
            x=k+nums[i]
            if x in d:
                if (x,nums[i]) not in m:
                    c+=1
                    p=(x,nums[i])
                    q=(nums[i],x)
                    m[p]=1
                    m[q]=1
            x=-k+nums[i]
            if x in d:
                if (x,nums[i]) not in m:
                    c+=1
                    p=(x,nums[i])
                    q=(nums[i],x)
                    m[p]=1
                    m[q]=1
            d[nums[i]]=d[nums[i]]+1 if nums[i] in d else 1
        return c