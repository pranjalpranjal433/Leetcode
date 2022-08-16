class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit1=0
        minval1=inf
        profit2=0
        minval2=inf
        for i in prices:
            minval1=min(minval1,i)
            profit1=max(profit1,i-minval1)
            minval2=min(minval2,i-profit1)
            profit2=max(profit2,i-minval2)
            # print(minval1,profit1,minval2,profit2)
        return profit2