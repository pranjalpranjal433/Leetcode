class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        a=[]
        s=0
        for i in range(len(nums)-1,-1,-1):
            a.append(s)
            s+=nums[i]
        s=0
        a.reverse()
        for i in range(len(nums)):
            left=s
            s+=nums[i]
            right=a[i]
            if left==right:
                return i
        return -1