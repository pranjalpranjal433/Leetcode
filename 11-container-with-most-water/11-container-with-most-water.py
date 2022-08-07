class Solution:
    def maxArea(self, height: List[int]) -> int:
        m=0
        i=0
        j=len(height)-1
        while(i<j):
            m=max(m,min(height[i],height[j])*(j-i))
            hl=min(height[i],height[j])
            while(i<j and hl>=height[i]):
                i+=1
            while(j>i and hl>=height[j]):
                j-=1
        return m