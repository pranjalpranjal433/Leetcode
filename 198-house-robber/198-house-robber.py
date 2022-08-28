class Solution:
    def rob(self, nums: List[int]) -> int:
        l=len(nums)
        if l<2:
            return nums[0]
        dp=[0]*l
        dp[0]=nums[0]
        dp[1]=max(dp[0],nums[1])
        for i in range(2,l):
            dp[i]=max(nums[i]+dp[i-2],dp[i-1])
        return dp[l-1]