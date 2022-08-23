class Solution:
    def maxLength(self, arr: List[str]) -> int:
        d={}
        d['ans']=0
        a={}
        for i in range(97,97+26):
            a[chr(i)]=0
            
        def can_place(ind):
            for i in arr[ind]:
                if a[i]==1:
                    return False
            ta={}
            for i in range(97,97+26):
                ta[chr(i)]=0
                
            for i in arr[ind]:
                if ta[i]==0:
                    ta[i]=1
                else:
                    return False
            return True
        
        def insert(ind):
            for i in arr[ind]:
                a[i]=1
                    
        def remove(ind):
            for i in arr[ind]:
                a[i]=0

        def find(ind,l):
            if ind == len(arr):
                d['ans']=max(d['ans'],l)
                return
            find(ind+1,l)
            if can_place(ind):
                insert(ind)
                find(ind+1,l+len(arr[ind]))
                remove(ind)
        find(0,0)
        return d['ans']