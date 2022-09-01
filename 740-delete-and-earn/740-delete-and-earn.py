class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        numss=[]
        nums.sort()
        numss.append(nums[0])
        l=nums[0]
        freq=[]
        c=1
        for i in range(1,len(nums)):
            if l!=nums[i]:
                numss.append(nums[i])
                freq.append(c)
                l=nums[i]
                c=1
            else:
                c+=1
        freq.append(c)
        dp=[0]*len(numss)
        dp[0]=numss[0]*freq[0]
        if len(numss)==1:
            return dp[0]
        dp[1]=numss[1]*freq[1] if numss[0]+1==numss[1] else (numss[0]*freq[0])+(numss[1]*freq[1])
        dp[1]=max(dp[0],dp[1])
        for i in range(2,len(numss)):
            dp[i]=(numss[i]*freq[i])+dp[i-2] if numss[i-1]+1==numss[i] else dp[i-1]+(numss[i]*freq[i])
            dp[i]=max(dp[i-1],dp[i])
        return dp[len(numss)-1]