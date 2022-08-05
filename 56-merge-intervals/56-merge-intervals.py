class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        a=[]
        s=intervals[0][0]
        e=intervals[0][1]
        for i in intervals:
            if(e>=i[0]):
                e=i[1] if i[1]>e else e
            else:
                a.append([s,e])
                s=i[0]
                e=i[1]
        a.append([s,e])
        return a