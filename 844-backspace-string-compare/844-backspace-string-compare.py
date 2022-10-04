class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a=[]
        for i in s:
            if i!='#':
                a.append(i)
            else:
                if len(a):
                    a.pop()
        str1=''
        for i in a:
            str1+=i
        b=[]
        for i in t:
            if i!='#':
                b.append(i)
            else:
                if len(b):
                    b.pop()
        str2=''
        for i in b:
            str2+=i
        return str1==str2
            