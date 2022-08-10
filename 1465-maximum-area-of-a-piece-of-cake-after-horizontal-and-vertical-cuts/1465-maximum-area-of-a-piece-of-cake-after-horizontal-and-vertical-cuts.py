class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        verticalCuts.append(0)
        verticalCuts.append(w)
        horizontalCuts.sort()
        verticalCuts.sort()
        x=0
        y=0
        mod=10**9+7
        for i in range(1,len(horizontalCuts)):
            x=max(x,horizontalCuts[i]-horizontalCuts[i-1])
        for i in range(1,len(verticalCuts)):
            y=max(y,verticalCuts[i]-verticalCuts[i-1])
        ans=(x%mod*y%mod)%mod
        return ans
        
        