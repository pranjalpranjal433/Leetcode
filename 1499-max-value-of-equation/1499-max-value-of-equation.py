from heapq import *
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        heap=[]
        ans=-inf
        for i in points:
            while heap and abs(i[0]-heap[0][1])>k:
                heappop(heap)
            if heap:
                ans=max(ans,-heap[0][0]+i[0]+i[1])
            heappush(heap,(-(i[1]-i[0]),i[0]))
        return ans