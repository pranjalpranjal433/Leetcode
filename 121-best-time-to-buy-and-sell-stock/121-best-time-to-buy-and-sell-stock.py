class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        m=prices[0]
        for i in prices:
            ans=max(ans,i-m)
            m=min(m,i)
        return ans