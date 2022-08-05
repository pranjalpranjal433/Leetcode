class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums)==0:
            return 0
        c=0
        p=1
        for i in nums:
            if i==0:
                c+=1
                continue
            p=p*i
        a=[]
        for i in nums:
            if c>1:
                a.append(0)
                continue
            if c==1:
                if i==0:
                    a.append(p)
                else:
                    a.append(0)
            else:
                a.append(p//i)
        return a
        