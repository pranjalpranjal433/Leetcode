class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        s=0
        ans=0;
        n=len(cardPoints)
        for i in range(n-k,n):
            s+=cardPoints[i]
        ans=s
        p=0
        for i in range(n-k,n):
            s=s-cardPoints[i]+cardPoints[p]
            p+=1
            ans=max(ans,s)
        return ans